# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
from task_cog import TaskManager
from db_setup import db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


# prefix is !
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@bot.command(name='hi', help='responds with :flushed:')
async def send_flushed(ctx):
    response = ":flushed:"
    await ctx.channel.send(response)


bot.run(TOKEN)