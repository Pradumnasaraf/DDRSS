import feedparser


url = "https://api.daily.dev/rss/b/36b73af8-f6cc-4b03-8ffc-a0aa6544b57f"
allEnetries = feedparser.parse(url)["entries"]

for entry in allEnetries:
    print(entry["link"])