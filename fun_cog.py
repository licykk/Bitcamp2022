from discord.ext import commands
import discord
from models import manager, Task 

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #add, delete, view
    @commands.command(name='dumbass', help='sometimes people need to be mocked')
    async def add_task(self, ctx, argv):
        await ctx.channel.send("Fun task!")
