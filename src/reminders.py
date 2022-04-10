import discord
from discord.ext import commands
import datetime as DT
import re
import time

#remind @blank 0m0d before task OR date/time with MESSAGE



class Reminder(commands.Cog):

    def __init__(self,bot, input):
        self.bot = bot
        client = discord.Client()

    @commands.command
    async def on_message(self, message):
        if message.content.startswith('!remind'):
            channel = message.channel
            await channel.send('Say hello!')

        def check(input):
            self.ex = re.match('to ("(?P<message>.*)")? on (?P<date>\d\d\/\d\d\/\d\d).*at (?P<time>\d\d:\d\d) ?(?P<apm>pm|am)',input)
            self.recievers = re.findall('@(\S*)', input)
            return (self.ex != None) and (self.recievers != None)

        msg = await client.wait_for('message', check=check)

        date = DT.datetime.strptime(self.ex.group('date'), '%m/%d/%y')
        time = DT.datetime.strptime(self.ex.group('time')+self.ex.group('apm'), '%I:%M%p')
        self.dt = DT.datetime.combine(date, time)
        self.message = self.ex.group('message')

        await time.asyncio.sleep(self.dt-DT.datetime.now())
        embed = discord.Embed(title=self.message)
        #for x in self.recievers:
        #    x.send(embed = embed)
        channel.send(embed = embed)


    @commands.command(name='remind_format')
    async def remind_format(self):
        print('!remind @Khaleesi @JonSnow to "you are literally related" on 04/09/22 at 9:00 pm')
