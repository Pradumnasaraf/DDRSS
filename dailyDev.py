import feedparser

def getAllFeed(url):
    description = ""
    allEnetries = feedparser.parse(url)["entries"]
    for entry in allEnetries:
        fstring = entry["link"] + "\n"
        a = fstring.split('?')
        description += a[0]+ "\n"
    return description
