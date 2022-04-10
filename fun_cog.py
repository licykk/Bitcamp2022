from discord.ext import commands
import discord
from models import manager, Task 

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #add, delete, view
    @commands.command(name='dumbass', help='sometimes people need to be mocked')
    async def add_task(self, ctx, argv):
        params = list(argv)
        new_task = Task(len(manager[ctx.message.channel.name].tasks) + 1, #id
                        params[0], #name
                        params[1], #priority
                        params[2] if len(params) >=3 else None, #assignment
                        params[3] if len(params) >=4 else None, #due_date
                        params[4] if len(params) >=5 else None) #status
                
        manager[ctx.message.channel.name].tasks.append(new_task)
        await ctx.channel.send("Added task to todo list!")
    
    
    @commands.command(name='delete', help='delete a task from the todo list!')
    async def delete_task(self, ctx, arg1):   
        task_list = manager[ctx.message.channel.name].tasks
        
        for i in range(0, len(task_list)):
            if task_list[i] == arg1:
                task_list.remove(i)
                
        await ctx.channel.send("Deleted task from todo list!")
