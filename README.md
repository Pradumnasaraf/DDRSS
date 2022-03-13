<img align="right" src="https://user-images.githubusercontent.com/51878265/158046499-30013c0f-9fab-41cf-aad3-71c48c82c2f8.gif" height=150px>
<h1> Daily Dev  Really Simple Syndication (DDRSS) Bot</h1>

**DDRSS Bot is a user specific Discord Bot**, which help user to get all bookmarks,  and latest bookmark on their discord chat. It aslo comes with search feature to find all the bookmarks which matches specfic keyword.
<br/>

> This Bot works on [`daily.dev`](https://daily.dev/) bookmark URL as source data (which user has to provide by a command).

## Bot development and existence.

**RSS Feed** returns XML data, which is complicated and cannot use directly into apps and programs other that webiste, by using `feedparser` Python packages, I have converted the data in `JSON` format, which is now easily extractbale,  and usable in building any kind of Apps and Bot (in our case).

Bot is extracting data like username, Blog/Artcile links, and title and return those data accordingly in proper pre-structued message, depedning on the command which thr user input.

## Using the Bot:

- <img align ="right" src="https://user-images.githubusercontent.com/51878265/158052899-f3e0760e-cef5-4eeb-bf47-1d9e2e5b2ee4.png"> Fisrt you need to invite the DDRSS Bot to the server, you can simply slick on the the right button 👉
- Sett your daily.dev Bookmark URL by using command 

### Commands:

Bot use (**`/`**) as prefix, that's every command will start with a slash (**`/`**)

- **`/allcmd`** - Returns all the DDRSS Bot command

- **`/serurl <your bookmark URL>`** - To set the the Bookmark URL (RSS Feed URL).

- **`/bm`** - Returns your latest 5 Bookmarks.

- **`/latestbm`** - Returns latest bookmark.

- **`/dd`** - Returns a short description about daily.dev.

- **`/searchbm <Keyword>`** <keyword> Returns the bookmarks matching that Keyword
  
  Eg: `/searchbm Open Source`
  
### Features:
  
  - User Specifc - By User Specifc means, strorning the user data indivisually with their ID's
  - Search Function - User easily find their Bookmarked blog with the simple command `.searchbm <Keyword>`
---



### Aim

It's built to prove the concept that how **RSS Feed** can be so powerful and useful when we have to share the **bulk** of data and also get the **latest data/feed** from the source. 


