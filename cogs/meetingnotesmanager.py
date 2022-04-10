from distutils.text_file import TextFile
from discord.ext import commands, tasks
import discord

from datetime import datetime
import os
import re

from models import *

def make_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

class MeetingNotesManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None and len(after.channel.members) == 1 and after.channel.name != "General":
            
            now = datetime.now()
            year = '{:02d}'.format(now.year)
            month = '{:02d}'.format(now.month)
            day = '{:02d}'.format(now.day)
            hour = '{:02d}'.format(now.hour)
            minute = '{:02d}'.format(now.minute)
            overall_date = '{}-{}-{}-{}-{}'.format(year, month, day, hour, minute)
            
            name = str(after.channel.name) +"-"+ overall_date +"-meeting"
            cat = discord.utils.get(member.guild.channels, name=after.channel.name, type=discord.ChannelType.text).category
            c = await cat.create_text_channel(name)
            await c.send(f"Created channel {name}")
            vc = after.channel
            self.die.start(c, vc, member.guild)

    
    @tasks.loop(seconds=5.0)
    async def die(self, curr_channel, vc, guild):
        if len(vc.members) == 0: 
            ### transcribe text channel ###
            txtfilename = curr_channel.name
            
            project_name = vc.name
            
            project_channel = discord.utils.get(guild.channels, name=project_name, type=discord.ChannelType.text) 
            
            # Initialize notes file add file name to notes file if it does not exist
            #if txtfile not in manager[project_name].notes:
            #    manager[project_name].notes.append(txtfile)
                
            make_dir('notes')
            make_dir('notes/{}'.format(project_name))
            with open(f'notes/{project_name}/{txtfilename}', 'w+') as meeting_notes:
                print("finished open")
        
                # Write messages to notes file
                async for message in curr_channel.history(limit=10, oldest_first=True):
                    # Write messages to files
                    if message.content is not None:
                        meeting_notes.write(message.content)
                        meeting_notes.write('\n')
                        await project_channel.send(message.content)

            embed_desc=f'Notes for {curr_channel} saved at {txtfilename}'
            embed=discord.Embed(title="NOTICE", description=embed_desc, color=0xFF5733)
            await project_channel.send(embed=embed)
            
            #delete current channel
            await curr_channel.delete() 
            self.die.cancel()


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

