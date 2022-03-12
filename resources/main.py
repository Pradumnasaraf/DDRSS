from email import message
import os
from discord.ext import commands
import discord
import feedparser
from dotenv import load_dotenv
import dailyDev

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
userData ={}

bot = commands.Bot(command_prefix=".", help_command=None)

def urlPrompt(ctx):
    message = f"Hey! 👋 {ctx.message.author.mention},\nPlease first set your **Daily.dev Bookmark URL**\n(By - **`.seturl`**), to use other commands!"
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
    global userData
    # Add the User data in the dictionary in format {discordUserID: bookmarkURL}
    userData[ctx.message.author.id] = userInputUrl
    message = await ctx.send(f"Hey {ctx.message.author.mention},\nyour *Bookmark URL* has been added :)")
    emoji = '\N{Black Heart}'
    await message.add_reaction(emoji)
   

@bot.command()
async def bm(ctx):

    # Check if the UserID is present in our userData Dic (Exception Handeling: KeyError)
    if ctx.message.author.id in userData:
        
        # userData[ctx.message.author.id] will return URL as the value.
        bookmarkOwner, bookmarks  = dailyDev.getBookmarks(userData[ctx.message.author.id])
        embed = discord.Embed(title=bookmarkOwner, description=bookmarks, color=0xffffff)
        embed.set_thumbnail(url=dailyDev.ddLogo)
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=urlPrompt(ctx))    


@bot.command()
async def searchbm(ctx, keyword):
    if ctx.message.author.id in userData:

        bookmarks  = dailyDev.seachPost(userData[ctx.message.author.id],keyword)
        # If user has no bookmark related to the user entred keyword:
        if bookmarks == "":
            await ctx.send("Nothing mached! :(, try something new")
        else:
            embed = discord.Embed(title=f"Bookmark's matching with your keyword : '{keyword}'", description=bookmarks, color=0xffffff)
            embed.set_thumbnail(url="https://user-images.githubusercontent.com/51878265/157502629-3a5d9b14-00e5-45f2-9b2e-b90ffee977bc.png")
            await ctx.send(embed=embed)       
    else:
        await ctx.send(embed=urlPrompt(ctx))
        
@bot.command()
async def latestbm(ctx):
    if ctx.message.author.id in userData:
        recentBookmark  = dailyDev.getLatestBookmark(userData[ctx.message.author.id])
        await ctx.send(recentBookmark)
    else:
        await ctx.send(embed=urlPrompt(ctx))

@bot.command()
async def dd(ctx):
    embed = discord.Embed(title="daily.dev", description=dailyDev.dd_desc, color=0xffffff)
    embed.set_thumbnail(url=dailyDev.ddLogo)
    message = await ctx.send(embed=embed)
    emoji = '\N{Black Heart}'
    await message.add_reaction(emoji)
        
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")