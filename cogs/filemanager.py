from discord.ext import commands
import discord
from models import * 

class FileManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.num_files = 0
    
    @commands.command(name='store', help='store files')
    async def store_file(self, ctx, *argv):        
        params = list(argv)
        file_list = manager[ctx.message.channel.name].files

        new_file = File(int(file_list[-1].id) + 1 if len(file_list) != 0 else 1, #id
                        params[0], #name
                        params[1]) #file                
                
        file_list.append(new_file)
        await ctx.channel.send("Stored file " +params[0]+ "!")

    
        
    @commands.command(name='view', help='view all stored files!')
    async def view_file(self, ctx):
        embed=discord.Embed(title="FILES", url="", description="", color=0xFF5733)
        file_list = manager[ctx.message.channel.name].files

        for file in file_list:
                embed.add_field(name=file.name, value=file.file, inline=False)

        await ctx.channel.send(embed=embed)


# class FileManager(commands.Cog):
#     def __init__(self, bot):
#         self.bot = bot
#         self.num_files = 0
    
#     @commands.command(name='store', help='store files')
#     async def store_file(self, ctx, *argv):
#         self.num_files += 1
#         with open('csv_files/files.csv', 'a', newline='') as f:
#             writer = csv.writer(f) 
#             writer.writerow([ctx.message.channel.name, self.num_files] + list(argv))   
        
#         await ctx.channel.send("Stored file!")
    
        
#     @commands.command(name='view', help='view all stored files!')
#     async def view_file(self, ctx):
#         embed=discord.Embed(title="FILES", url="", description="", color=0xFF5733)

#         with open('csv_files/files.csv', 'r') as f:
#             for row in csv.reader(f):
#                 print(row)
#                 if row[0] == ctx.message.channel.name:
#                     embed.add_field(name=row[2], value=row[3], inline=False)

#         await ctx.channel.send(embed=embed)

def setup(bot):
    return bot.add_cog(FileManager(bot))

