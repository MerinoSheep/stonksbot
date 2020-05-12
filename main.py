#main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import tickerprice
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')

@bot.command()
async def stonk(ctx,arg):
	is_found, stock_info = tickerprice.given_ticker(arg)#stock info will return price and url in a tuple
	if(not is_found):
		await ctx.send(stock_info[0])
	else:
		embed = discord.Embed(title="Stock", color=0x08b2e3)
		embed.set_thumbnail(url=stock_info[1])
		embed.add_field(name="Price:", value=stock_info[0], inline=False)
		embed.set_footer(text="Logos provided by Clearbit(https://clearbit.com)")
		
		await ctx.send(embed=embed)

@bot.event
async def on_ready():
	guild = discord.utils.get(bot.guilds, name=GUILD)
	await bot.change_presence(activity=discord.Game(name="the stock market📉")) #Emoji is chart decreasing
bot.run(TOKEN)