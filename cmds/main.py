import discord
from discord.ext import commands
from core.classes import Core


class Main(Core):
    @commands.command()
    async def ping(self,ctx):
     await ctx.send(F"{round(self.bot.latency*1000)} (ms)")


def setup(bot):
    bot.add_cog(Main(bot))
