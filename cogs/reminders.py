import discord
from discord.ext import commands
import datetime as DT
import re
import time

#remind @blank 0m0d before task OR date/time with MESSAGE

client = discord.Client()

class Reminder(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name = 'remind')
    async def remind(self,ctx):
        await ctx.send('okay what reminder do you want?')
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        msg = await self.bot.wait_for('message', check=check)
        if msg.content=='q':
            await ctx.send('woooowww you don\'t want a reminder? enjoy your f')
        else:
            date_ = DT.datetime.strptime(self.ex.group('date'), '%m/%d/%y')
            time_ = DT.datetime.strptime(self.ex.group('time')+self.ex.group('apm'), '%I:%M%p')
            self.dt = DT.datetime.combine(date_.date(), time_.time())
            self.message = self.ex.group('message')

            while self.dt < DT.datetime.now():
                print('here')
                time.sleep(1)
            embeded = discord.Embed(title=self.message)

            async def name_to_user_object(self, ctx, user: discord.Member):
                print(type(user)) 
                return user

            for x in self.recievers:
                whose_dm = '<@' + x + '>'
                await name_to_user_object(self, ctx, whose_dm).send(embed=embeded)
                #await ctx.send(embed = embed)


    @commands.command(name='remind_format')
    async def remind_format(self):
        print('!remind @Khaleesi @JonSnow to "you are literally related" on 04/09/22 at 9:00 pm')

def setup(bot):
    return bot.add_cog(Reminder(bot))
