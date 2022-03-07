import os
from discord.ext import commands
import discord
import feedparser
from dotenv import load_dotenv
import dailyDev

load_dotenv()

TOKEN = os.environ.get('DISCORD_TOKEN')
url = "https://api.daily.dev/rss/b/36b73af8-f6cc-4b03-8ffc-a0aa6544b57f"

bot = commands.Bot(command_prefix="$", help_command=None)

@bot.event
async def on_ready():
    print("We have logged in as {}".format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send("Hey {}".format(ctx.message.author.mention))

@bot.command()
async def allfeeds(ctx, userURL):
    allentries  = dailyDev.getAllFeed(userURL)
    embed = discord.Embed(title="Current value of ", description=allentries, color=0x66acba)
    # .set_thumbnail(url="")
    await ctx.send(embed=embed)

try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")
