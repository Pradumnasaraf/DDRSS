import feedparser
ddLogo = "https://user-images.githubusercontent.com/51878265/157502629-3a5d9b14-00e5-45f2-9b2e-b90ffee977bc.png"
dd_desc ="**daily.dev** is the fastest growing online community for developers to stay updated on the best developer news. Together we supercharge developers' knowledge and empower better software.\n https://daily.dev/"

bot_logo = "https://user-images.githubusercontent.com/51878265/158382703-da9f59d2-c55b-47f2-ab39-ef53177a9b3e.png"

# Max post to return, by default it's 5
maxPost = 0
def getBookmarks(url):
    global maxPost
    maxPost = 5
    return f"{bookmarkOwner(url)}'s Bookmarks - daily.dev", getPosts(url)

def getLatestBookmark(url):
    global maxPost
    maxPost = 1
    return f"> {bookmarkOwner(url)}'s Latest Bookmark - daily.dev\n\n{getPosts(url)} "

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

def allcmd():
    cmd= '''
Bot use (/) as a prefix, that's every command will start with a slash (/)

/allcmd - Returns all the DDRSS Bot command

/serurl <your sharable bookmark URL> - To set the the Bookmark URL (RSS Feed URL).

/bm - Returns your latest 5 Bookmarks.

/latestbm - Returns latest bookmark.

/dd - Returns a short description about daily.dev.

/searchbm <Keyword> Returns the bookmarks matching that Keyword    
''' 
    return cmd