from discord.ext import commands
import discord
from db_setup import db
import csv

class TaskManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.num_files = 0
    
    #add, delete, view
    @commands.command(name='add', help='adds a task to the todo list!')
    async def add_task(self, ctx, *argv):
        self.num_files += 1
        with open('csv_files/tasks.csv', 'a',  newline='') as f:
            writer = csv.writer(f)                               # create the csv writer
            writer.writerow([ctx.message.channel.name, self.num_files] + list(argv))   # write a row to the csv file

        await ctx.channel.send("Added task to todo list!")
    
    
    @commands.command(name='delete', help='deletes a task from the todo list!')
    async def delete_task(self, ctx, arg1):
        with open('csv_files/files.csv', 'r') as f:
            for row in csv.reader(f):
                if row[0] == ctx.message.channel.name and row[1] == arg1:
                    row[0] = "XXX" #deleting is too expensive!
                    row[1] = "XXX"
                    
        await ctx.channel.send("Deleted task from todo list!")
        
        
    @commands.command(name='todo', help='view alltasks in todo list!')
    async def view_tasks(self, ctx, *args):
        channel_tasks = []
        
        with open('csv_files/tasks.csv', 'r') as f:
            for row in csv.reader(f):
                if row[0] == ctx.message.channel.name:
                    channel_tasks.append("Task:" +row[2]+ "~~~~~" + "SOMETHING ELSE:" +row[3])

                    # channel_tasks.append(row[0:])
        
        print(channel_tasks)
        await ctx.channel.send('\n'.join(channel_tasks))
        
def setup(bot):
    return bot.add_cog(TaskManager(bot))

