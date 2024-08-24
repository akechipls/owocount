import discord
from discord.ext import commands, tasks

class countOwO(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.count.start()

    @tasks.loop(seconds=1.0)
    async def count(self):
        print('a loop has passed')
        channels = ['1275360317739765800', '795635457412562977']

        for channel in channels:
            try:
                cnl = self.bot.get_channel(int(channel))
                await cnl.send('a loop has passed')
            except Exception as e:
                print(e)


def setup(bot):
    bot.add_cog(countOwO(bot))