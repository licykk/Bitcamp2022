from discord.ext import commands
import discord
from models import manager, Task 

class TaskManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='add', help='add a task to the todo list!')
    async def add_task(self, ctx, *argv):
        params = list(argv)
        task_list = manager[ctx.message.channel.name].tasks
        new_task = Task(int(task_list[-1].id) + 1 if len(task_list) != 0 else 1, #id
                        params[0], #name
                        params[1], #priority
                        params[2] if len(params) >=3 else None, #assignment
                        params[3] if len(params) >=4 else None, #due_date
                        params[4] if len(params) >=5 else None) #status
                
                
        task_list.append(new_task)
        await ctx.channel.send("Added task to todo list!", delete_after=3)    
    
    @commands.command(name='delete', help='delete a task from the todo list!')
    async def delete_task(self, ctx, taskid_to_be_deleted):   
        task_list = manager[ctx.message.channel.name].tasks
        
        for i in range(0, len(task_list)):
            if int(task_list[i].id) == int(taskid_to_be_deleted):
                task_list.pop(i)
                break
                
        await ctx.channel.send("Deleted task from todo list!", delete_after=3)
        
        
    @commands.command(name='todo', help='view all tasks in todo list!')
    async def view_tasks(self, ctx):
        task_list = manager[ctx.message.channel.name].tasks
        embed=discord.Embed(title="TASKS", url="", description="", color=0xFF5733)
        for t in task_list:
            embed.add_field(name=t.id, value=f'Description: {t.name}\nPriority: {t.priority}\nStatus: {t.status}\nAssignment: {t.assignment}\nDue Date: {t.due_date}',inline=True)

        await ctx.channel.send(embed=embed)
        
def setup(bot):
    return bot.add_cog(TaskManager(bot))

