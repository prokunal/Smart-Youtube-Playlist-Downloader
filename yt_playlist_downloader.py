# Author: Kunal Kumar
# Social: twitter.com/l1v1n9h311, instagram.com/prokunal
# Website: procoder.in

from pytube import YouTube
from pytube import Playlist
from math import ceil
import sys
import threading

try:
    p = Playlist(sys.argv[1])
except:
    print('usage: python3 {} url'.format(__file__.split('/')[-1]))
    sys.exit(0)
#global links
print("Playlist Name : {}\nChannel Name  : {}\nTotal Videos  : {}\nTotal Views   : {}".format(p.title,p.owner,p.length,p.views))
links = []
size = 0
try:
    for url in p.video_urls:
        links.append(url)
except:
    print('Playlist link is not valid.')
    sys.exit(0)
l1 = ceil(len(links)/4)

link1 = links[0:l1]
link2 = links[l1:l1+l1]
link3 = links[l1+l1:l1+l1+l1]
link4 = links[l1+l1+l1:l1+l1+l1+l1]

print("Downloading Started...\n")
def downloader1():
    for i in link1:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 1 -->  " + filename.split('/')[-1] + ' Downloaded')

def downloader2():
    for i in link2:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 2 -->  " + filename.split('/')[-1] + ' Downloaded')

def downloader3():
    for i in link3:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 3 -->  " + filename.split('/')[-1] + ' Downloaded')

def downloader4():
    for i in link4:
      yt = YouTube(i)
      ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 4 -->  " + filename.split('/')[-1] + ' Downloaded')

t1 = threading.Thread(target=downloader1, name='d1')
t2 = threading.Thread(target=downloader2,name='d2')
t3 = threading.Thread(target=downloader3, name='d3')
t4 = threading.Thread(target=downloader4,name='d4')
t1.start()
t2.start()
t3.start()
t4.start()

