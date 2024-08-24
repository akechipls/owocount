import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self,ctx):
        await ctx.send("sosi")

def setup(bot):
    bot.add_cog(Ping(bot))