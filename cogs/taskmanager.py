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
        await ctx.channel.send("Added task to todo list!")
    
    
    @commands.command(name='delete', help='delete a task from the todo list!')
    async def delete_task(self, ctx, taskid_to_be_deleted):   
        task_list = manager[ctx.message.channel.name].tasks
        
        for i in range(0, len(task_list)):
            if int(task_list[i].id) == int(taskid_to_be_deleted):
                task_list.pop(i)
                break
                
        await ctx.channel.send("Deleted task from todo list!")
        
        
    @commands.command(name='todo', help='view all tasks in todo list!')
    async def view_tasks(self, ctx):
        task_list = manager[ctx.message.channel.name].tasks
        embed=discord.Embed(title="TASKS", url="", description="", color=0xFF5733)
        for t in task_list:
            embed.add_field(name=t.id, value=f'Description: {t.name}\nPriority: {t.priority}\nStatus: {t.status}\nAssignment: {t.assignment}\nDue Date: {t.due_date}',inline=True)

        await ctx.channel.send(embed=embed)

    # @commands.command(name='add', help='add a task to the todo list!')
    # async def add_task(self, ctx, *argv):
    #     self.num_files += 1
    #     with open('csv_files/tasks.csv', 'a',  newline='') as f:
    #         writer = csv.writer(f)                               
    #         writer.writerow([ctx.message.channel.name, self.num_files] + list(argv))   # write a row to the csv file

    #     await ctx.channel.send("Added task to todo list!")
    
    
    # @commands.command(name='delete', help='delete a task from the todo list!')
    # async def delete_task(self, ctx, arg1):    
    #     with open('csv_files/new_tasks.csv', 'w', newline='') as f2:
    #         writer = csv.writer(f2)
    #         with open('csv_files/tasks.csv', 'r') as infile:
    #             for row in csv.reader(infile):  # content is all the other lines
    #                 if row[1] != arg1:
    #                     writer.writerow(row)
        
    #     os.remove('csv_files/tasks.csv')
    #     os.rename(r'csv_files/new_tasks.csv',r'csv_files/tasks.csv')

    #     await ctx.channel.send("Deleted task from todo list!")
        
        
    # @commands.command(name='todo', help='view all tasks in todo list!')
    # async def view_tasks(self, ctx, *argv):
    #     embed=discord.Embed(title="TASKS", url="", description="", color=0xFF5733)
    #     with open('csv_files/tasks.csv', 'r') as f:
    #         for row in csv.reader(f):
    #             print(row)
    #             if row[0] == ctx.message.channel.name:
    #                 # embed.add_field(name=row[1], value=row[2], inline=False)
    #                 embed.add_field(name=row[1], value=f'Description: {row[2]}\nPriority: {row[3]}\nAssignment: {row[4]}',inline=True)

    #     await ctx.channel.send(embed=embed)

        
def setup(bot):
    return bot.add_cog(TaskManager(bot))

