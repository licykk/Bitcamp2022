from discord import CategoryChannel
from discord.ext import commands
from models import *

class ProjectManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='p', help='creates a new project')
    async def make_project(self, ctx, proj_name):
        guild = ctx.guild
        cat = await guild.create_category(proj_name, position=0)
        await cat.create_text_channel(proj_name)
        await cat.create_voice_channel(proj_name)
        manager[proj_name] = Project(proj_name)

        # send message in project-selection
        sel = discord.utils.get(guild.channels, name="project-selection")
        await sel.send(proj_name)


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


    # @commands.Cog.listener()
    # async def on_raw_reaction_add(self, payload):
    #     channel = await self.bot.fetch_channel(payload.channel_id)
    #     message = await channel.fetch_message(payload.message_id)
    #     user = await self.bot.fetch_user(payload.user_id)
    #     emoji = payload.emoji

    #     await channel.send("Hello")


    # @commands.Cog.listener
    # async def on_raw_reaction_add(self, reaction, user):  
    #     if reaction.emoji == '👍':   
    #         await reaction.message.channel.send(reaction.message)
    #     else:
    #         await reaction.message.channel.send("NOPE") 
      
        # if reaction.message.channel.name == "project-selection":
        #     print(reaction.message)
    # #         await reaction.message.channel.send(reaction.message)
    # #         # if str(reaction.emoji):
    # #         #     manager[reaction.message.content].members.append(user.id)

    # #             # await user.add_roles(Role)


def setup(bot):
    return bot.add_cog(ProjectManager(bot))