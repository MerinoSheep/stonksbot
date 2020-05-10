#main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')

@bot.command()
async def stonk(ctx,*arg):
	await ctx.send(arg)
@bot.event
async def on_ready():
	guild = discord.utils.get(bot.guilds, name=GUILD)
	await bot.change_presence(activity=discord.Game(name="the stock market📉")) #Emoji is chart decreasing
bot.run(TOKEN)