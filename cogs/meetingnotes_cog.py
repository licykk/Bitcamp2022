from discord.ext import commands
import discord
import re
import os
from models import *

def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

class MeetingNotesManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='transcribe', help='store all meeting notes in a file')
    async def store_notes(self, ctx):     
        
        notes_channel_name = ctx.message.channel.name
        
        # extract original project name from notes channel name
        m = re.match(r"(.*)-meeting-notes", notes_channel_name)
        channel_name = m[1]
        channel = discord.utils.get(ctx.guild.channels, name=channel_name) 
        
        # Initialize notes file add file name to notes file if it does not exist
        if notes_filename not in manager[channel_name].notes:
             manager[channel_name].notes.append(notes_filename)
        make_dir('notes')
        make_dir('notes/{}'.format(channel_name))
        notesfile = open('notes/{}/{}'.format(channel_name, notes_filename), 'w')
        
        # Write messages to notes file
        async for message in ctx.channel.history(limit=None, oldest_first=True):
            # Write messages to files
            if message.content is not None:
                notesfile.write(message.content)
                notesfile.write('\n')
                #await channel.send(message.content)

        embed_desc='Notes for {} saved at {}'.format(notes_filename)
        embed=discord.Embed(title="NOTICE", description=embed_desc, color=0xFF5733)
        await channel.send(embed=embed)
        notesfile.close()

    @commands.command(name='noteslist', help='view all tasks in todo list!')
    async def list_notes(self, ctx):
        
        project = ctx.message.channel.name
        
        if project not in manager:
            await ctx.channel.send('No meeting notes found!')
            return
        
        for filename in manager[project].notes:
            await ctx.channel.send(filename)
        
def setup(bot):
    return bot.add_cog(MeetingNotesManager(bot))

