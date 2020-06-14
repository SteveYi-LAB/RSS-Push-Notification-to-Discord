import feedparser
import requests
from urllib.parse import *

a_empty ="1"

webhook_url = ''
rss_url = ''
rss = feedparser.parse(rss_url)
old = (rss.entries[0]['link'])

while a_empty != 1 :
  rss = feedparser.parse(rss_url)
  channel_name = (rss['feed']['title'])
  video_name = (rss['entries'][0]['title'])
  video_link = (rss.entries[0]['link'])
  new = (rss.entries[0]['link'])
  if old != new : 
    a = 'https://api.yiy.tw/DISCORD/webhook.php?url=' + (webhook_url) + '&avatar_url=https://static.yiy.tw/media/logo/Yi_logo.png&content=' + (channel_name) + '發佈了影片啦！趕快來看看吧～' + (video_name) + (video_link)
    requests.get(a)
    old = (rss.entries[0]['link'])
print ("success")
