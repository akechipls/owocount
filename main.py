import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('TOKEN')

bot = discord.Bot()

@bot.slash_command()
async def ping1(ctx):
    name = ctx.author.name
    await ctx.respond(f"Hello {name}")

for filename in os.listdir('./cogs'):
        try:
            bot.load_extension('cogs.backgroundTask')
        except Exception as e:
            print(e)

bot.run(TOKEN)