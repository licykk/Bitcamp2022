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
        with open('csv_files/tasks.csv', 'r+') as f:
            for row in csv.reader(f):
                if row[0] == ctx.message.channel.name and row[1] != arg1:
                    print(row)
                    row[0] = "XXX" #deleting is too expensive!
                    row[1] = "XXX"
        
        await ctx.channel.send("Deleted task from todo list!")
        
        
    @commands.command(name='todo', help='view alltasks in todo list!')
    async def view_tasks(self, ctx, *argv):
        embed=discord.Embed(title="TASKS", url="", description="", color=0xFF5733)
        with open('csv_files/tasks.csv', 'r') as f:
            for row in csv.reader(f):
                print(row)
                if row[0] == ctx.message.channel.name:
                    # embed.add_field(name=row[1], value=row[2], inline=False)
                    embed.add_field(name=row[1], value=f'Description: {row[2]}\nPriority: {row[3]}\nAssignment: {row[4]}',inline=True)

        await ctx.channel.send(embed=embed)

        


