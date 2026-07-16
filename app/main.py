import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import dailyDev

load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
userData = {}

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Prompt message if the user URL is not present
def urlPrompt(user):
    message = f"Hello! 👋 {user.mention},\nPlease set your **daily.dev sharable bookmark URL** first\n(By - **`/seturl`**), before using other commands!.\n\n**If you dont have the URL, refer this link**\n🎥 - https://bit.ly/3CK8kvG."
    embed = discord.Embed(description=message, color=0xff0000)
    return embed


@client.event
async def on_ready():
    await tree.sync()
    print(f"DDRSS Bot have logged in as ${client.user}, let's rock")


@tree.command(name="ddrss", description="To check the ddrss bot is alive or not")
async def ddrss(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention} I'm Alive (:")


@tree.command(name="allcmd", description="Returns a list of all ddrss Bot commands.")
async def allcmd(interaction: discord.Interaction):
    embed = discord.Embed(title="DDRSS Bot Commands:", description=dailyDev.allcmd(), color=0xffffff)
    embed.set_thumbnail(url=dailyDev.bot_logo)
    await interaction.response.send_message(embed=embed)


@tree.command(name="seturl", description="To set user daily dev rss bookmark url")
async def seturl(interaction: discord.Interaction, url: str):
    global userData

    # Check if the user entered URL is daily.dev RSS feed url or not
    if "api.daily.dev/rss" in url:
        # Add the User data in the dictionary in format {discordUserID: bookmarkURL}
        userData[interaction.user.id] = url
        await interaction.response.send_message(f"Hey {interaction.user.mention},\nyour *Bookmark URL* has been added, now you can use other commands :)")
        # For adding the reaction.
        message = await interaction.original_response()
        emoji = '\N{Rocket}'
        await message.add_reaction(emoji)
    else:
        url_error_description = "**Look like you have entered wrong URL,\nplease try setting it up again**"
        embed = discord.Embed(title="URL Error:", description=url_error_description, color=0xff0000)
        await interaction.response.send_message(embed=embed)


@tree.command(name="bookmarks", description="Return user bookmarked posts (limit -5)")
async def bookmarks(interaction: discord.Interaction):

    # Check if the UserID is present in our userData Dic (Exception Handeling: KeyError)
    if interaction.user.id in userData:

        # userData[interaction.user.id] will return URL as the value.
        bookmarkOwner, bookmarks = dailyDev.getBookmarks(userData[interaction.user.id])
        embed = discord.Embed(title=bookmarkOwner, description=bookmarks, color=0xffffff)
        embed.set_thumbnail(url=dailyDev.ddLogo)
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(embed=urlPrompt(interaction.user))


@tree.command(name="latestbm", description="Rreturns the user's latest bookmarked post")
async def latestbm(interaction: discord.Interaction):
    if interaction.user.id in userData:
        recentBookmark = dailyDev.getLatestBookmark(userData[interaction.user.id])
        await interaction.response.send_message(recentBookmark)
    else:
        await interaction.response.send_message(embed=urlPrompt(interaction.user))


@tree.command(name="searchbm", description="Search and returns user bookmarked posts matching the specific keywor")
async def searchbm(interaction: discord.Interaction, keyword: str):

    # check if the user URL is present in our dic.
    if interaction.user.id in userData:
        bookmarks = dailyDev.seachPost(userData[interaction.user.id], keyword)

        # If user has no bookmark matched to the user entred keyword:
        if bookmarks == "":
            await interaction.response.send_message("Nothing matched! :(, try something new")
        else:
            embed = discord.Embed(title=f"Bookmark's matching with keyword : _{keyword}_", description=bookmarks, color=0xffffff)
            embed.set_thumbnail(url=dailyDev.ddLogo)
            await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message(embed=urlPrompt(interaction.user))


@tree.command(name="dailydev", description="Returns a short description about daily dev")
async def dailydev(interaction: discord.Interaction):
    embed = discord.Embed(title="daily.dev", description=dailyDev.dd_desc, color=0xE0B0FF)
    embed.set_thumbnail(url=dailyDev.ddLogo)
    await interaction.response.send_message(embed=embed)
    message = await interaction.original_response()
    emoji = '\N{Fire}'
    await message.add_reaction(emoji)


try:
    client.run(TOKEN)
except discord.errors.LoginFailure:
    print("Login unsuccessful.")
