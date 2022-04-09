from discord.ext import commands
import discord
from models import Task
from db_setup import db

class TaskManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #add, delete, view
    @commands.command(name='add', help='adds a task to the todo list!')
    async def add_task(self, ctx, *args):
        new_task = Task(
            name= args[0],
        )
        
            # priority= args[2] if len(args) >= 2 else None,
            # assignment = args[3] if len(args) >= 3 else None,
            # due_date = args[4] if len(args) >= 4 else None,
        new_task.save()

        db.tasks.insert_one(new_task) #store response in db but how to specify which project?
        await ctx.channel.send("Added task to todo list!")
    
    
    @commands.command(name='delete', help='deletes a task from the todo list!')
    async def delete_task(self, ctx, arg1):
        db.tasks.deleteMany( { id: arg1 } )
        await ctx.channel.send("Deleted task from todo list!")
        
        
    @commands.command(name='todo', help='view alltasks in todo list!')
    async def view_tasks(self, ctx, *args):
        if not args:
            await ctx.channel.send(db.tasks.find().pretty())
        else:
            return None


