from email import message
import discord
from discord.ext import commands, tasks
import datetime as DT
import re
import time

#remind @blank 0m0d before task OR date/time with MESSAGE

client = discord.Client()

class Reminder(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'remind')
    async def remind(self, ctx):
        await ctx.send('okay what reminder do you want?')

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        msg = await self.bot.wait_for('message', check=check, timeout=None)

        content = msg.content

        if content=='q':
            await ctx.send('woooowww you don\'t want a reminder? enjoy your f')
        else:
            date = msg.created_at
            created = str(date).split(" ")
            date_ = created[0]
            time_ = created[1]

            recievers = msg.mentions

            embeded = discord.Embed(title=content, url="", description="", color=0xFF5733)

            async def name_to_user_object(self, ctx, user: discord.Member):
                print(type(user)) 
                return user

            for x in recievers:
                await x.send(embed=embeded)
                #await ctx.send(embed = embed)


    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1


    @commands.command(name='remind_format')
    async def remind_format(self):
        print('!remind @Khaleesi @JonSnow to "you are literally related" on 04/09/22 at 9:00 pm')

def setup(bot: commands.Bot):
    bot.add_cog(Reminder(bot))
