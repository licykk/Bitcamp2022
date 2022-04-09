import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client["discord_project_manager"]
