import os
from discord.ext import commands
import discord
import feedparser
from dotenv import load_dotenv
import dailyDev

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
userData ={}
userUrl=""

bot = commands.Bot(command_prefix=".", help_command=None)

def urlPrompt():
    message = "Hey! 👋,\nPlease first set your **Daily.dev Bookmark URL**\n(By - **`.seturl`**), to use other commands!"
    embed = discord.Embed(description=message, color=0xff0000)
    return embed

@bot.event
async def on_ready():
    print("We have logged in as {}".format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hey {ctx.message.author.mention}")

@bot.command()
async def seturl(ctx, userInputUrl):
    global userUrl
    userUrl= {userInputUrl}
    bookmarkOwner = dailyDev.bookmarkOwner(userInputUrl)
    await ctx.send(f"Hey, {bookmarkOwner},\nyou are all set (:")

@bot.command()
async def bm(ctx):
    if userUrl == "":
        await ctx.send(embed=urlPrompt())
    else:
        bookmarkOwner, bookmarks  = dailyDev.getBookmarks(userUrl)
        embed = discord.Embed(title=bookmarkOwner, description=bookmarks, color=0xffffff)
        embed.set_thumbnail(url="https://user-images.githubusercontent.com/51878265/157502629-3a5d9b14-00e5-45f2-9b2e-b90ffee977bc.png")
        await ctx.send(embed=embed)
    
@bot.command()
async def searchbm(ctx, keyword):
    if userUrl == "":
        await ctx.send(embed=urlPrompt())
    else:
        bookmarks  = dailyDev.seachPost(userUrl,keyword)
        if bookmarks == "":
            await ctx.send("Nothing mached! :(, try something new")
        else:
            embed = discord.Embed(title=f"Bookmark's matching with your keyword : '{keyword}'", description=bookmarks, color=0xffffff)
            embed.set_thumbnail(url="https://user-images.githubusercontent.com/51878265/157502629-3a5d9b14-00e5-45f2-9b2e-b90ffee977bc.png")
            await ctx.send(embed=embed)
        
@bot.command()
async def latestbm(ctx):
    if userUrl == "":
        await ctx.send(embed=urlPrompt())
    else:
        recentBookmark  = dailyDev.getLatestBookmark(userUrl)
        await ctx.send(recentBookmark)

try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")