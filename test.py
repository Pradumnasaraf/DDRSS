import feedparser


url = "https://api.daily.dev/rss/b/36b73af8-f6cc-4b03-8ffc-a0aa6544b57f"
allEnetries = feedparser.parse(url)

print(allEnetries["bozo"])

print(allEnetries["feed"]["title"])

@bot.command()
async def allfeeds(ctx, userURL):
    allentries  = dailyDev.getAllFeed(userURL)
    embed = discord.Embed(title="Current value of ", description=allentries, color=0x66acba)
    embed.add_field(name="Fiel1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=True)
    # .set_thumbnail(url="")
    await ctx.send(embed=embed)@bot.command()
async def allfeeds(ctx, userURL):
    allentries  = dailyDev.getAllFeed(userURL)
    embed = discord.Embed(title="Current value of ", description=allentries, color=0x66acba)
    embed.add_field(name="Fiel1", value="hi", inline=False)
    embed.add_field(name="Field2", value="hi2", inline=True)
    # .set_thumbnail(url="")
    await ctx.send(embed=embed)

