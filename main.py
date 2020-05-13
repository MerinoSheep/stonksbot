# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import tickerprice
import sql_stock
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')


@bot.command()
async def stonk(ctx, arg):
	stock_info = sql_stock.find_entry(arg)
	if stock_info != None:
		embed = discord.Embed(title=stock_info[1], color=0x08b2e3)  # Name of stock
		embed.set_thumbnail(url=stock_info[2])
		embed.add_field(name="Price:", value=tickerprice.get_price(arg), inline=False)
		embed.set_footer(
			text="Logos provided by Clearbit(https://clearbit.com)")

		await ctx.send(embed=embed)
	else:
		is_found, stock_info = tickerprice.given_ticker(arg)
		if(not is_found):
			await ctx.send(stock_info[0])#Returns error message
		else:
			embed = discord.Embed(title=stock_info[2], color=0x08b2e3)  # Name of stock
			if stock_info[1] != 'None':
				embed.set_thumbnail(url=stock_info[1]) #Icon
				embed.add_field(name="Price:", value=stock_info[0], inline=False) #Price
				embed.set_footer(
					text="Logos provided by Clearbit(https://clearbit.com)")
				sql_stock.add_entry(arg,stock_info[2],stock_info[1])
				await ctx.send(embed=embed)


@bot.event
async def on_ready():
	guild = discord.utils.get(bot.guilds, name=GUILD)
	# Emoji is chart decreasing
	await bot.change_presence(activity=discord.Game(name="the stock market📉"))
bot.run(TOKEN)
