import requests
import discord
from discord.ext import commands
import datetime
from models import *

URL = "https://www.googleapis.com/calendar/v3/freeBusy"



class ScheduleManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




def setup(bot):
    return bot.add_cog(ScheduleManager(bot))