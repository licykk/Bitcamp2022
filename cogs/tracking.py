import discord
from discord.ext import commands

class Tracking(commands.Cog):
    def __init__(self, bot):
        self.bot = bot # This is so you can access Bot instance in your cog

# You must have this function for `bot.load_extension` to call
def setup(bot):
    bot.add_cog(Tracking(bot))