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
        channel_files = []
        
        with open('csv_files/files.csv', 'r') as f:
            for row in csv.reader(f):
                print(row)
                if row[0] == ctx.message.channel.name:
                    channel_files.append("Name:" +row[2]+ "~~~~~" + "URL:" +row[3])

        print(channel_files)
        await ctx.channel.send('\n'.join(channel_files))

def setup(bot):
    return bot.add_cog(FileManager(bot))

