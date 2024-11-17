import webbrowser
from random import choice
import feedparser

def entertain_grace():
    channel = feedparser.parse("https://www.youtube.com/feeds/videos.xml?channel_id=UCFMbX7frWZfuWdjAML0babA")
    vid = choice(channel.entries)
    webbrowser.open_new(vid.link)