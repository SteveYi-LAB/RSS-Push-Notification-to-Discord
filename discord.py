import feedparser
import requests
from urllib.parse import *

a_empty = "1"

webhook_url = ''
rss_url = ''
rss = feedparser.parse(rss_url)
old = (rss.entries[0]['link'])
json_content = {
    "content": "Bot has been start!",
    "username": "",
    "avatar_url": "",
    "tts": "false"
}
requests.post(webhook_url, json_content)
print("Bot is Start!")
while a_empty != 1:
    rss = feedparser.parse(rss_url)
    channel_name = (rss['feed']['title'])
    video_name = (rss['entries'][0]['title'])
    video_link = (rss.entries[0]['link'])
    new = (rss.entries[0]['link'])
    if old != new:
        json_content = {
            "content": ""+ video_link,
            "username": "",
            "avatar_url": "",
            "tts": "false"
        }
        requests.post(webhook_url, json_content)
        old = (rss.entries[0]['link'])
print("Bot is Stop!")
