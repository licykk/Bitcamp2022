from discord.ext import commands

class Project(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='project', help='creates a new project')
    async def project():
        pass


def setup(bot):
    return bot.add_cog(Project(bot))