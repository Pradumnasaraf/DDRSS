import feedparser
ddLogo = "https://user-images.githubusercontent.com/51878265/157502629-3a5d9b14-00e5-45f2-9b2e-b90ffee977bc.png"

dd_desc ="**daily.dev** is the fastest growing online community for developers to stay updated on the best developer news. Together we supercharge developers' knowledge and empower better software.\n🌐 - https://daily.dev/"

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
    commands_list= '''
**/ddrss** - to check wether the bot is alive or not.
**/allcmd** - returns a list of all DDRSS Bot commands.
**/serurl <your sharable bookmark URL>** - to set user daily dev rss bookmark url.
**/bookmarks** - returns all of the user's bookmarked post (latest - 5 post).
**/latestbm** - returns the user's latest bookmarked post.
**/searchbm <Keyword>** - search and returns user bookmarked posts matching the specific keyword. 
**/dailydev** - returns a short description about daily dev  
''' 
    return commands_list
