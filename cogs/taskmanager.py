from discord.ext import commands
import discord
from models import *

class TaskManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='add', help='add a task to the todo list!')
    async def add_task(self, ctx, *argv):

        # print error message if task name not given
        if argv:
            task_name = ' '.join(argv)
        else:
            embed=discord.Embed(title="Error", description="Usage: add1 [task name]", color=0xFF5733)
            await ctx.send(embed=embed)
            return
        
        channel = ctx.message.channel.name

        # get username of user that ran command
        user = ctx.message.author

        # standard check for message from DM channel
        def check(ctx):
            return lambda msg: msg.author == ctx.author and isinstance(msg.channel, discord.DMChannel)
    
        # get user input from DM channel with customizable validation function
        async def get_input(prompt, validation_func, ctx, user):
            while True:
                await user.send(prompt)
                try:
                    msg = await self.bot.wait_for('message', check=check(ctx))
                    output = validation_func(msg.content)
                    if output is ValueError:
                        continue
                    return output
                except ValueError:
                    continue
        
        # validation function for priority value        
        def check_priority(msg_content):
            try:
                msg_content = int(msg_content)
                if msg_content >= 1 and msg_content <= 5:
                    return msg_content
                else:
                    return ValueError
            except:
                return ValueError
        
        # prompt user to input values for each attribute of a task
        priority_prompt = 'Input Priority Value for task "{}" (Note: 1 = most important and 5 = most important):'.format(task_name)
        priority = await get_input(priority_prompt, check_priority, ctx, user)
        #await ctx.channel.send(str(priority))
        assignee = await get_input('Input Assignee for task "{}":'.format(task_name), str, ctx, user)
        #await ctx.channel.send(assignee)
        due_date = await get_input('Input Due Date for task "{}":'.format(task_name), str, ctx, user)
        #await ctx.channel.send(due_date)

        #print("adding task")
        task_list = manager[channel].tasks
        new_task = Task(int(task_list[-1].id) + 1 if len(task_list) != 0 else 1, #id
                        task_name, #name
                        priority, #priority
                        assignee, #assignment
                        due_date, #due_date
                        "Incomplete") #status       
                
        #print("added task")
        task_list.append(new_task)
        await ctx.channel.send('Added task "{}" to todo list!'.format(task_name))
        await user.send('User {} added task "{}" to todo list!'.format(user, task_name))
        await ctx.channel.send("Added task to todo list!")
        #await ctx.channel.delete(delay=3)
    
    
    @commands.command(name='delete', help='delete a task from the todo list!')
    async def delete_task(self, ctx, taskid_to_be_deleted):   
        task_list = manager[ctx.message.channel.name].tasks
        
        for i in range(0, len(task_list)):
            if int(task_list[i].id) == int(taskid_to_be_deleted):
                task_list.pop(i)
                break
                
        await ctx.channel.send("Deleted task from todo list!")
        #await ctx.channel.delete(delay=3)
        
    @commands.command(name='edit', help='update a task from the todo list!')
    async def edit_task(self, ctx, taskid_to_be_edited, field, new_value):   
        
        if field not in ['name', 'priority', 'assignee', 'due_date']:
            await ctx.channel.send("Invalid field name! Choose one of: ['name', 'priority', 'assignee', 'due_date']")
            return
        
        task_list = manager[ctx.message.channel.name].tasks
        
        for i in range(0, len(task_list)):
            if int(task_list[i].id) == int(taskid_to_be_edited):
                if field == 'name':
                    task_list[i].name = new_value
                elif field == 'priority':
                    task_list[i].priority = new_value
                elif field == 'assignee':
                    task_list[i].assignment = new_value
                elif field == 'due_date':
                    task_list[i].due_date = new_value
                await ctx.channel.send("Updated task from todo list!")
                break
                
        #await ctx.channel.delete(delay=3)
        
    @commands.command(name='completed', help='update status of a task from the todo list!')
    async def mark_task_complete(self, ctx, taskid_to_be_updated):   
        
        task_list = manager[ctx.message.channel.name].tasks
        
        for i in range(0, len(task_list)):
            if int(task_list[i].id) == int(taskid_to_be_updated):
                task_list[i].status = "Complete"
                await ctx.channel.send("Updated task status!")
                break
                
        #await ctx.channel.delete(delay=3)
        
    @commands.command(name='todo', help='view incomplete tasks in todo list!')
    async def view_tasks(self, ctx):
        task_list = manager[ctx.message.channel.name].tasks
        embed=discord.Embed(title="TO-DO", url="", description="", color=0xFF5733)
        for t in task_list:
            if t.status == "Incomplete":
                embed.add_field(name=t.id, value=f'Description: {t.name}\nPriority: {t.priority}\nStatus: {t.status}\nAssignment: {t.assignment}\nDue Date: {t.due_date}',inline=True)

        await ctx.channel.send(embed=embed)
        
    @commands.command(name='alltasks', help='view all tasks in todo list!')
    async def view_tasks(self, ctx):
        task_list = manager[ctx.message.channel.name].tasks
        embed=discord.Embed(title="ALL TASKS", url="", description="", color=0xFF5733)
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

