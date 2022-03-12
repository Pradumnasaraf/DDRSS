import feedparser

# Max post to return, by default it's 4
maxPost = 0

def getBookmarks(url):
    global maxPost
    maxPost = 5
    return f"{bookmarkOwner(url)}'s Bookmarks - Daily.dev", getPosts(url)

def getLatestBookmark(url):
    global maxPost
    maxPost = 1
    return f"> {bookmarkOwner(url)}'s Latest Bookmark - Daily.dev\n\n{getPosts(url)} "

def bookmarkOwner(url):
    recivedTitle =feedparser.parse(url)["feed"]["title"]
    splittedString = recivedTitle.split("'s ")
    return splittedString[0]
    
def getPosts(url):
    ticker = 1
    description =""
    allEntries = feedparser.parse(url)["entries"]
    for entry in allEntries:
        if ticker <= maxPost:
            articleLink = entry["link"]
            splitedString = articleLink.split('?')
            articleTitle = f'**{entry["title"]}**'
            description += f"{articleTitle}\nPost Link: {splitedString[0]}\n\n"
            ticker += 1

    return description

def seachPost (url, keyword):
    description =""
    allEntries = feedparser.parse(url)["entries"]
    for entry in allEntries:
        articleTitle = entry["title"]
        if keyword.lower() in articleTitle.lower():
            articleLink = entry["link"]
            splitedString = articleLink.split('?')
            articleTitle = f'**{entry["title"]}**'
            description += f"{articleTitle}\nPost Link: {splitedString[0]}\n\n"
    return description


