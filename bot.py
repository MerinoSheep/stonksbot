# main.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import tick
import sql_db
from discord.ext.commands import CommandNotFound

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
bot = commands.Bot(command_prefix='!')

up_emoji = '\U00002668'
down_emoji = '\U0001F4A5'
def create_embed(ctx,arg,stock_info):
	price,pick_emoji = tick.get_price(arg)
	embed = discord.Embed(title=stock_info[1], color=0x08b2e3)  # Name of stock
	embed.set_thumbnail(url=stock_info[2])
	embed.add_field(name="Price:", value=price,inline=False)
	embed.set_footer(
		text="Logos provided by Clearbit(https://clearbit.com)")
	emoji = up_emoji if pick_emoji else down_emoji
	return embed,emoji
@bot.command()
async def stonk(ctx, *arg):
	if(not arg):
		await ctx.send("!stonk requires a parameter type a stock ticker")
		return;
	arg = arg[0].upper()
	stock_info = sql_db.find_entry(arg)
	if stock_info != None:
		embed,emoji = create_embed(ctx,arg,stock_info)
		msg = await ctx.send(embed=embed)
		await msg.add_reaction(emoji)
	else:
		is_found, stock_info = tick.given_ticker(arg)
		if(not is_found):
			await ctx.send(stock_info[0])#Returns error message
		else:
			embed = discord.Embed(title=stock_info[1], color=0x08b2e3)  # Name of stock
			if stock_info[1] != 'None':
				embed,emoji = create_embed(ctx,arg,stock_info)
				sql_db.add_entry(arg,stock_info[1],stock_info[2])
				print("Created Stock for {}".format(arg))
				msg = await ctx.send(embed=embed)
				await msg.add_reaction(emoji)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.event
async def on_ready():
	guild = discord.utils.get(bot.guilds, name=GUILD)
	# Emoji is chart decreasing
	await bot.change_presence(activity=discord.Game(name="the stock market📉"))
	print("Bot is ready")
bot.run(TOKEN)
