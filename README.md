<img align="right" src="https://user-images.githubusercontent.com/51878265/158046499-30013c0f-9fab-41cf-aad3-71c48c82c2f8.gif" height=150px>
<h1><img src="https://user-images.githubusercontent.com/51878265/158064566-853b9c0a-342f-4597-b88e-40a1cb9621cc.png" height=25>Daily Dev Really Simple Syndication (DDRSS) Bot</h1>

**DDRSS Bot is a user-specific Discord Bot**, which help user to get all bookmarks and the latest bookmark on their discord chat. It also comes with a search feature to find all the bookmarks which match specific keywords.
<br/>

> This Bot works on [`daily.dev`](https://daily.dev/) bookmark URL as source data (which user has to provide by a command).

<br/>

## 👨‍💻 Bot development and existence.

**RSS Feed** returns XML data, which is complicated and cannot use directly in apps and programs other than the website, by using `feedparser` Python packages, I have converted the data in `JSON` format, which is now easily extractable,  and usable in building any kind of Apps and Bot (in our case).

The bot is extracting data like username, Blog/Article links, and title and return those data accordingly in the proper pre-structured message, depending on the command which the user input

<br/>

## 🕹️ Using the Bot:

<img align ="right" src="https://user-images.githubusercontent.com/51878265/158052899-f3e0760e-cef5-4eeb-bf47-1d9e2e5b2ee4.png">**Step 1:** First you need to invite the Bot to the server, you can simply click on the right button 👉
 
**Step 2:** Set your [`daily.dev`](https://daily.dev/) Bookmark URL by using command - `/serurl <your sharable bookmark URL>`

<details>
 
 <summary> Click here: Tutorial for getting daily.dev Sharable Bookmark (RSS Feed link) </summary>

https://user-images.githubusercontent.com/51878265/158066794-5129f6f5-15ae-4b99-a764-e3e59bef8631.mp4
 <h6>Video Source - daily.dev Twitter<h6>
  
</details>

**Step 3:** It's done, now you can use a different slash command to perform the task.

<br/>

### ✍️ Commands:

Bot use (`/`) as a prefix, that's every command will start with a slash (`/`)

- `/allcmd` - Returns all the DDRSS Bot command

- `/serurl <your sharable bookmark URL>` - To set the the Bookmark URL (RSS Feed URL).

- `/bm` - Returns your latest 5 Bookmarks.

- `/latestbm` - Returns latest bookmark.

- `/dd` - Returns a short description about daily.dev.

- `/searchbm <Keyword>` <keyword> Returns the bookmarks matching that Keyword
  
  Eg: `/searchbm Open Source`
  
### ⭐ Features:
  
  - User Specific - By User Specific means, storing the user data individually with their ID's
  - Search Function - User easily find their Bookmarked blog with the simple command `/searchbm <Keyword>`
  - Error Handling - If user tried to to command like `/bm` or `/latestbm` without setting the URL, the bot will handle that.
  
  <p align="center"><img src="https://user-images.githubusercontent.com/51878265/158070808-7f2a0cb6-3d0e-4c14-88fa-2fb4aa6c9b53.png"></p>


### Aim of the project:

It's built to prove the concept that how **RSS Feed** can be so powerful and useful when we have to share the **bulk** of data and also get the **latest data/feed** from the source. 
  
