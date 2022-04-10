from discord.ext import commands
import discord
import csv

class FileManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.num_files = 0
    
    @commands.command(name='store', help='stores files')
    async def store_file(self, ctx, *argv):
        self.num_files += 1
        with open('csv_files/files.csv', 'a', newline='') as f:
            writer = csv.writer(f) 
            writer.writerow([ctx.message.channel.name, self.num_files] + list(argv))   
        
        await ctx.channel.send("Stored file!")
    
        
    @commands.command(name='view', help='view all stored files!')
    async def view_file(self, ctx):
        embed=discord.Embed(title="FILES", url="", description="", color=0xFF5733)

        with open('csv_files/files.csv', 'r') as f:
            for row in csv.reader(f):
                print(row)
                if row[0] == ctx.message.channel.name:
                    embed.add_field(name=row[2], value=row[3], inline=False)

        await ctx.channel.send(embed=embed)



