from pytube import YouTube
from sys import argv
import os

link = argv[1]
yt = YouTube(link)

print(f"Title: {yt.title}")
print(f"view: {yt.views}")

yd = yt.streams.get_highest_resolution()

os.makedirs("e:/youtube", exist_ok=True)


yd.download("e:/youtube")