# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
<<<<<<< HEAD
from cogs.taskmanager import TaskManager
from cogs.filemanager import FileManager
from db_setup import db
=======
from cogs.task_cog import TaskManager
from cogs.filemanager_cog import FileManager
>>>>>>> 20d1a833f56ca4458b77b064606a530b9c57cdf7

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# prefix is !
bot = commands.Bot(command_prefix='*')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user} is connected to the following guild:\n'
        # f'{guild.name}(id: {guild.id})'
    )

@bot.command(name='hi', help='responds with :flushed:')
async def send_flushed(ctx):
    response = ":flushed:"
    await ctx.channel.send(response)


if __name__ == "__main__":
    # When running this file, if it is the 'main' file
    # I.E its not being imported from another python file run this
    for file in os.listdir("cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            print(file)
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(TOKEN)