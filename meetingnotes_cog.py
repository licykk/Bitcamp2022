from discord.ext import commands
import discord
import csv

class MeetingNotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.num_files = 0
    
    @commands.command(name='start_meeting', help='stores files')
    async def on_ready(self, ctx, name):
        guild = ctx.message.guild
        if not name:
            await ctx.send('Sorry, but you have to insert a name. Try again, but do it like this: `>create [channel name]`')
        else:
            await guild.create_text_channel(name)
            await ctx.send(f"Created a channel named {name}")

        # server = ctx.message.server
        # await self.bot.create_channel(server, 'cool-channel', type=discord.ChannelType.text)
            
        
    # @commands.command(name='view', help='view all stored files!')
    # async def view_file(self, ctx):
    #     embed=discord.Embed(title="FILES", url="", description="", color=0xFF5733)

    #     with open('csv_files/files.csv', 'r') as f:
    #         for row in csv.reader(f):
    #             print(row)
    #             if row[0] == ctx.message.channel.name:
    #                 embed.add_field(name=row[2], value=row[3], inline=False)

    #     await ctx.channel.send(embed=embed)



