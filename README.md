<img align="right" src="https://user-images.githubusercontent.com/51878265/158046499-30013c0f-9fab-41cf-aad3-71c48c82c2f8.gif" height=150px>
<h1> Daily Dev  Really Simple Syndication (DDRSS) Bot</h1>

**DDRSS Bot is a Discord Bot**, that is built to prove the concept that how **RSS Feed** can be so powerful and useful when we have to share the bulk of data and also get the latest data/feed from the source. 

> Bot woks on [`daily.dev`](https://daily.dev/) bookmark URL as source data (which user has to provide by a command).

## Bot development and existence.

**RSS Feed** returns XML data, which is complicated and cannot use directly into apps and programs other that webiste, by using `feedparser` Python packages, I have converted the data in `JSON` format, which is now easily extractbale,  and usable in building any kind of Apps and Bot (in our case).

