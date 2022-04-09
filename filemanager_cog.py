from discord.ext import commands
import discord
from mongoengine import MongoEngine
from .models import File

class FileManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='store', help='stores files')
    async def store_file(self, ctx, filename, file):
        new_file = File(
            name=filename,
            file=file,
        )
        new_file.save()

        db.files.insert_one(file) #store response in db but how to specify which project?
        await ctx.channel.send("Stored " +file) #look at channel?
        
        
        
    @commands.command(self, name='view', help='view all stored files!')
    async def view_file(ctx):
        await ctx.channel.send(db.files.find().pretty())
        # mongo.db.files.insert_one(file) #store response in db
        # await ctx.channel.send("Stored " +file)



