from discord.ext import commands

class ProjectManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='p', help='creates a new project')
    async def make_project(self, ctx, proj_name):
        guild = ctx.guild
        cat = await guild.create_category(proj_name, position=0)
        c = await cat.create_text_channel(proj_name)
        vc = await cat.create_voice_channel(proj_name)


def setup(bot):
    return bot.add_cog(ProjectManager(bot))