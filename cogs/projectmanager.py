import discord
from discord import CategoryChannel
from discord.ext import commands
from models import *
from discord.utils import get

class ProjectManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.name != "project-selection":
            return
        if message.author.bot:
            return
        proj_name = message.content
        guild = message.guild

        await guild.create_role(name=proj_name)

        role = get(guild.roles, name=proj_name)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            role: discord.PermissionOverwrite(read_messages=True)
        }

        cat = await guild.create_category(proj_name, position=0, overwrites=overwrites)
        await cat.create_text_channel(proj_name, overwrites=overwrites)
        await cat.create_voice_channel(proj_name, overwrites=overwrites)
        manager[proj_name] = Project(proj_name)
        await message.add_reaction('👍')


    @commands.command(name='d', help='deletes a new project')
    async def delete_project(self, ctx, *, category: CategoryChannel):
        delcategory = category
        channels = delcategory.channels
        
        for channel in channels: # We search for all channels in a loop
            try:
                await channel.delete() # Delete all channels
            except AttributeError: # If the category does not exist/channels are gone
                pass
        await delcategory.delete() 
        print(channels)


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = payload.member
        emoji = payload.emoji

        role = get(user.guild.roles, name = message.content)
        await user.add_roles(role)


def setup(bot):
    return bot.add_cog(ProjectManager(bot))