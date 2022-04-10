from discord.ext import commands
import discord

class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='add1', help='adds a task to the todo list!')
    async def add_task(self, ctx, *args):
        
        if args and args[0]:
            task_name = args[0]
        else:
            embed=discord.Embed(title="Error", description="Usage: add1 [task name]", color=0xFF5733)
            await ctx.send(embed=embed)
            return
        
        user = ctx.message.author
        
        def check_dm(msg):
            return msg.author == ctx.author and isinstance(msg.channel, discord.DMChannel)
        
        await user.send("Input Priority Value:")
        priority = await self.bot.wait_for("message", check=check_dm)
        
        await user.send("Input Assignee:")
        assignee = await self.bot.wait_for("message", check=check_dm)
        
        await user.send("Input Due Date:")
        due_date = await self.bot.wait_for("message", check=check_dm)
        
        # make sure response will only be registered if specific conditions are met
        #def check_priority(msg):
        #    return msg.author == ctx.author and msg.channel == ctx.channel and \
        #    msg.content.isdigit()

        #msg = await client.wait_for("message", check=check)
        #if msg.content.lower() == "y":
        #    await ctx.send("You said yes!")
        #else:
        #    await ctx.send("You said no!")
        
        await ctx.channel.send(name.content)
        await ctx.channel.send(task_name)
        await ctx.channel.send("Added task to todo list!")
    
    
    @commands.command(name='delete', help='deletes a task from the todo list!')
    async def delete_task(self, ctx, arg1):
        await ctx.channel.send("Deleted task from todo list!")
        
        
    @commands.command(name='todo', help='view all tasks in todo list!')
    async def view_tasks(self, ctx, *args):
        await ctx.channel.send("Viewing todo list")


