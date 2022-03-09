import os
from discord.ext import commands
import discord
import feedparser
from dotenv import load_dotenv
import dailyDev

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="/", help_command=None)

@bot.event
async def on_ready():
    print("We have logged in as {}".format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send("Hey {}".format(ctx.message.author.mention))

@bot.command()
async def allbm(ctx, userURL):
    bookmarkOwner, bookmarks  = dailyDev.getBookmarks(userURL)
    embed = discord.Embed(title=bookmarkOwner, description=bookmarks, color=0xffffff)
    embed.set_thumbnail(url="https://user-images.githubusercontent.com/51878265/157502629-3a5d9b14-00e5-45f2-9b2e-b90ffee977bc.png")
    await ctx.send(embed=embed)
    
@bot.command()
async def latestbm(ctx, userURL):
    recentBookmark  = dailyDev.getLatestBookmark(userURL)
    await ctx.send(recentBookmark)

try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")
