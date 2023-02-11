[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/Pradumnasaraf/DDRSS)

<div align="center">

<img src="https://user-images.githubusercontent.com/51878265/178142801-3e0cbdc1-e943-4f16-98af-cf74e2790165.png" height=200px>

<h1><img src="https://user-images.githubusercontent.com/51878265/158064566-853b9c0a-342f-4597-b88e-40a1cb9621cc.png" height=25>Daily Dev Really Simple Syndication (DDRSS) Bot</h1>

[![Publish Image to GitHub Container Registry](https://github.com/Pradumnasaraf/DDRSS/actions/workflows/publish-ghcr.yml/badge.svg)](https://github.com/Pradumnasaraf/DDRSS/actions/workflows/publish-ghcr.yml) [![Releases](https://github.com/Pradumnasaraf/DDRSS/actions/workflows/releases.yml/badge.svg)](https://github.com/Pradumnasaraf/DDRSS/actions/workflows/releases.yml)

**DDRSS Bot is a user-specific Discord Bot**, which help user to get all bookmarks and the latest bookmark on their discord chat. It also comes with a search feature to find the bookmarks which match the specific keywords.
<br>

</div>

> Bot works on [`daily.dev`](https://daily.dev/) shareable bookmark URL as source data.

<br>

<b><h3 align="center">🎉 Winner project of <a href="https://twitter.com/dailydotdev/status/1507003555110027276?s=20&t=1jqwj4nvk0KO6uuMStV1Ig">daily.dev RSS Feed Hackathon.</a>🎉 </h3></b>

## 👨‍💻 Bot development and existence.

**RSS Feed** returns XML data, which is complicated and cannot use directly in apps and programs other than the website, by using `feedparser` -a  Python package, I have converted the return data into `JSON` format, which is now easily extractable, and usable in building any kind of Apps and Bot (in our case).

Every time user calls a command, the bot request data from the API `api.daily.dev/rss/a/*****`  (link vary user to user) and extract data like `username`, `Blog/Article links`, and `title`, and convert into `JSON` and return those data accordingly in the proper pre-structured message, depending on the command which the user input.

<br/>

## 🕹️ Using the Bot:

<a href="https://discord.com/oauth2/authorize?client_id=950398355853430824&permissions=414464661568&scope=bot%20applications.commands"><img align ="right" src="https://user-images.githubusercontent.com/51878265/158052899-f3e0760e-cef5-4eeb-bf47-1d9e2e5b2ee4.png"><a>**Step 1:** First you need to invite the Bot to the server, you can click on the right button for invite. 👉
 
**Step 2:** Set your [`daily.dev`](https://daily.dev/) sharable bookmark URL by using command - `/serurl <your sharable bookmark URL>`

<details>
 
 <summary> Click here: Tutorial for getting daily.dev Sharable Bookmark (RSS Feed link) </summary>

https://user-images.githubusercontent.com/51878265/158066794-5129f6f5-15ae-4b99-a764-e3e59bef8631.mp4
 <h6>Video Source - daily.dev Twitter<h6>
  
</details>

**Step 3:** It's done, now you can use a different slash command to perform the task.

<br/>

### ✍️ Commands:

Bot use (`/`) as a prefix, that's every command will start with a slash (`/`). Every command is integrated into Discord Slash commands
  
- `/ddrss` - to check whether the bot is working or not.
  
- `/allcmd` - returns a list of all DDRSS Bot commands.
  
- `/serurl <your sharable bookmark URL>` - will set the user daily dev rss bookmark url.
  
- `/bookmarks` - returns all of the user's bookmarked posts. (latest - 5 post).
  
- `/latestbm` - returns the user's latest bookmarked post.
  
- `/dailydev` - returns a short description about daily.dev
  
 - `/searchbm <Keyword>` - search and returns user bookmarked posts matching that specific keyword.
  
  Eg: `/searchbm Open Source`
  
  
## ⭐ Features:
  
  - **User-specific** - By user-specific it means returning data type varies from user to user.
  - **Slash commands** - Uses Slash commands, commands are directly integrated into the Discord message box, we don't need to remember any of the commands. Typing `/` will show up all the commands.
   
  <p align="center"><img src="https://user-images.githubusercontent.com/51878265/158960622-766606bc-d7d8-45cb-9f76-a14d90cd0c30.png"></p>
   
  - **Search function** - User can easily find their bookmarked posts, with the simple command `/searchbm <Keyword>`
  - **Error handling** - If a user tried to use the command like `/bm` or `/latestbm` without setting up the URL or setting up the wrong URL, the bot will handle that, and prompt them.
  
  <p align="center"><img src="https://user-images.githubusercontent.com/51878265/158960290-0bd28630-32bd-4b2d-b74f-f614607d1543.png"></p>

## 📹 Tutorial

To get an overview and working of the Bot, please check out the video (By clicking the **Thumbnail/Image** below).
  
  <p align="center"><a href="https://youtu.be/y9EkAZh2TtA"><img height="300" src="https://user-images.githubusercontent.com/51878265/158964027-932a81fd-870e-4235-bb40-98ef6f2259d1.png"><a></p>
   

## 🖱️ Using the project:

- Fork this repository
 
- Install all the dependencies from [`requirements.txt`](/resources/requirements.txt) file. We can also use the command to install all the dependencies at once.

```sh
pip3 install -r requirements.txt 
```

- Create a `.env` file in the root folder and add your Discord Token and like so, get the keys by creating a bot application in the [Discord Developer Portal](https://discord.com/developers/applications)
   
```txt
DISCORD_TOKEN =   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
   
- Invite the bot to the server, with sending message and slash command permissions.

<details>
 
 <summary>Like this</summary>
 
![Image](https://user-images.githubusercontent.com/51878265/162361445-19b5f99e-6ec4-416c-a44a-461fb5d756a0.png)

</details>

- Run `python3 main.py` in the terminal for running the bot.
  
## 🎯 Aim of the project:

This project was built to prove the concept that how **RSS Feed** can be so powerful and useful when we have to share, transfer and use **bulk** of data and also fetch the **latest data/feed** from the source. 

---
   
### 🎉 Winner project of daily.dev RSS Feed Hackathon.
   
<p align ="center"><img src=https://user-images.githubusercontent.com/51878265/162356966-daa57aed-1e7a-4048-b62b-bddf20b4b72b.png height="800"></p>

