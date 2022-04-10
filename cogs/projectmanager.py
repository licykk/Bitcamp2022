from discord.ext import commands

class ProjectManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='p', help='creates a new project')
    async def make_project(self, ctx, proj_name):
        pass


def setup(bot):
    return bot.add_cog(ProjectManager(bot))