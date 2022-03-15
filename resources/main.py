import os
from discord.ext import commands
import discord
import feedparser
from dotenv import load_dotenv
from discord_slash import SlashCommand, SlashContext
import dailyDev

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
userData ={}

bot = commands.Bot(command_prefix="/", help_command=None)
slash = SlashCommand(bot,sync_commands=True)

def urlPrompt(ctx):
    message = f"Hey! 👋 {ctx.author.mention},\nPlease first set your **Daily.dev Bookmark URL**\n(By - **`/seturl`**), to use other commands!"
    embed = discord.Embed(description=message, color=0xff0000)
    return embed

@bot.event
async def on_ready():
    print("We have logged in as {}".format(bot.user))

@slash.slash(name="DDRRSS")
async def DDRSS(ctx):
    await ctx.send(f"Hey {ctx.author.mention} I'm Alive (:")

 
@slash.slash(name="seturl")
async def seturl(ctx, url):
    global userData
    # Add the User data in the dictionary in format {discordUserID: bookmarkURL}
    userData[ctx.author.id] = url
    message = await ctx.send(f"Hey {ctx.author.mention},\nyour *Bookmark URL* has been added :)")
    emoji = '\N{Black Heart}'
    await message.add_reaction(emoji)


@slash.slash(name="searchbm")
async def searchbm(ctx, keyword):
    if ctx.author.id in userData:
        bookmarks  = dailyDev.seachPost(userData[ctx.author.id],keyword)
        # If user has no bookmark related to the user entred keyword:
        if bookmarks == "":
            await ctx.send("Nothing mached! :(, try something new")
        else:
            embed = discord.Embed(title=f"Bookmark's matching with keyword : '{keyword}'", description=bookmarks, color=0xffffff)
            embed.set_thumbnail(url="https://user-images.githubusercontent.com/51878265/157502629-3a5d9b14-00e5-45f2-9b2e-b90ffee977bc.png")
            await ctx.send(embed=embed)       
    else:
        await ctx.send(embed=urlPrompt(ctx))

  
@slash.slash(name="bookmarks")
async def bookmarks(ctx):
    # Check if the UserID is present in our userData Dic (Exception Handeling: KeyError)
    if ctx.author.id in userData:
        # userData[ctx.message.id] will return URL as the value.
        bookmarkOwner, bookmarks  = dailyDev.getBookmarks(userData[ctx.author.id])
        embed = discord.Embed(title=bookmarkOwner, description=bookmarks, color=0xffffff)
        embed.set_thumbnail(url=dailyDev.ddLogo)
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=urlPrompt(ctx))   
        
@slash.slash(name="latestbm")
async def latestbm(ctx):
    if ctx.author.id in userData:
        recentBookmark  = dailyDev.getLatestBookmark(userData[ctx.author.id])
        await ctx.send(recentBookmark)
    else:
        await ctx.send(embed=urlPrompt(ctx))


@slash.slash(name="dailydev")
async def dailydev(ctx):
    embed = discord.Embed(title="daily.dev", description=dailyDev.dd_desc, color=0xffffff)
    embed.set_thumbnail(url=dailyDev.ddLogo)
    await ctx.send(embed=embed)


@slash.slash(name="allcmd", description ="Return all DDRSS Bot commands.")
async def allcmd(ctx):
    embed = discord.Embed(title="DDRSS Bot Commands:", description=dailyDev.allcmd(), color=0xffffff)
    embed.set_thumbnail(url=dailyDev.bot_logo)
    await ctx.send(embed=embed)
       
try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")