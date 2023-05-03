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

# Propmpt message is user URL is not present 
def urlPrompt(ctx):
    message = f"Hello! 👋 {ctx.author.mention},\nPlease set your **daily.dev sharable bookmark URL** first\n(By - **`/seturl`**), before using other commands!.\n\n**If you dont have the URL, refer this link**\n🎥 - https://bit.ly/3CK8kvG."
    embed = discord.Embed(description=message, color=0xff0000)
    return embed

@bot.event
async def on_ready():
    print(f"DDRSS Bot have logged in as ${bot.user}, let's rock")

@slash.slash(name="ddrss", description="To check the ddrss bot is alive or not")
async def ddrss(ctx):
    await ctx.send(f"Hey {ctx.author.mention} I'm Alive (:")


@slash.slash(name="allcmd", description ="Returns a list of all ddrss Bot commands.")
async def allcmd(ctx):
    embed = discord.Embed(title="DDRSS Bot Commands:", description=dailyDev.allcmd(), color=0xffffff)
    embed.set_thumbnail(url=dailyDev.bot_logo)
    await ctx.send(embed=embed)
       

@slash.slash(name="seturl", description="To set user daily dev rss bookmark url")
async def seturl(ctx, url):
    global userData

    # Check if the user entered URL is daily.dev RSS feed url or not
    if "api.daily.dev/rss" in url: 
        # Add the User data in the dictionary in format {discordUserID: bookmarkURL}
        userData[ctx.author.id] = url
        message = await ctx.send(f"Hey {ctx.author.mention},\nyour *Bookmark URL* has been added, now you can use other commands :)")
        # For adding the reaction
        emoji = '\N{Rocket}'
        await message.add_reaction(emoji)
    else:
        url_error_description = "**Look like you have entered wrong URL,\nplease try setting it up again**"
        embed = discord.Embed(title="URL Error:", description=url_error_description, color=0xff0000)
        await ctx.send(embed=embed)

@slash.slash(name="bookmarks",description ="Return user bookmarked posts (limit -5)")
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


@slash.slash(name="latestbm", description ="Rreturns the user's latest bookmarked post")
async def latestbm(ctx):
    if ctx.author.id in userData:
        recentBookmark  = dailyDev.getLatestBookmark(userData[ctx.author.id])
        await ctx.send(recentBookmark)
    else:
        await ctx.send(embed=urlPrompt(ctx))


@slash.slash(name ="searchbm", description="Search and returns user bookmarked posts matching the specific keywor")
async def searchbm(ctx, keyword):

    # check if the user URL is present in our dic.
    if ctx.author.id in userData:
        bookmarks  = dailyDev.seachPost(userData[ctx.author.id],keyword)

        # If user has no bookmark matched to the user entred keyword:
        if bookmarks == "":
            await ctx.send("Nothing matched! :(, try something new")
        else:
            embed = discord.Embed(title=f"Bookmark's matching with keyword : _{keyword}_", description=bookmarks, color=0xffffff)
            embed.set_thumbnail(url=dailyDev.ddLogo)
            await ctx.send(embed=embed)       
    else:
        await ctx.send(embed=urlPrompt(ctx))


@slash.slash(name="dailydev", description ="Returns a short description about daily dev")
async def dailydev(ctx):
    embed = discord.Embed(title="daily.dev", description=dailyDev.dd_desc, color=0xE0B0FF)
    embed.set_thumbnail(url=dailyDev.ddLogo)
    message = await ctx.send(embed=embed)
    emoji = '\N{Fire}'
    await message.add_reaction(emoji)


try:
    bot.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Login unsuccessful.")