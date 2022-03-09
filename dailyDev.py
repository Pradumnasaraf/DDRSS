from typing_extensions import final
import feedparser

def getBookmarks(url):
    return bookmarkOwner(url), getAllFeed(url)

def bookmarkOwner(url):
    recivedTitle =feedparser.parse(url)["feed"]["title"]
    splittedString = recivedTitle.split("by ")
    return f"{(splittedString[0]).title()}({splittedString[1]})"
    
def getAllFeed(url):
    description =""
    allEntries = feedparser.parse(url)["entries"]
    for entry in allEntries:
        articleLink = entry["link"]
        splitedString = articleLink.split('?')
        articleTitle = f'**{entry["title"]}**'
        description += f"{articleTitle}\nPost Link: {splitedString[0]}\n\n"
    return description