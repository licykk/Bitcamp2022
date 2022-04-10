from discord.ext import commands, tasks
import discord
from datetime import datetime

class MeetingNotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel is None and after.channel is not None:
            name =  str(after.channel.name) +"-"+ str(datetime.now()) +"-meeting!!"
            c = await member.guild.create_text_channel(name)
            await c.send(f"Created a channel named {name}")
            vc = after.channel
            
            #eric's code :D
            
            
            
                    
            self.die.start(c, vc)
                    
            
    @tasks.loop(seconds=5.0)
    async def die(self, c, vc):
        print("owo")
        if len(vc.members) == 0:
            #delete
            await c.delete()        

def setup(bot):
    return bot.add_cog(MeetingNotes(bot))

