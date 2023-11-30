# Author: Kunal Kumar
# Social: twitter.com/l1v1n9h311, instagram.com/prokunal
# Website: procoder.in

from pytube import YouTube
from pytube import Playlist
from math import ceil
import sys
import threading

try:
    p = Playlist(input("Enter Playlist URL: "))
except:
    pass
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
size = ceil(len(links)/4)
def split_link(links,size):
    for i in range(0,len(links),size):
        yield links[i:i+size]
link = list(split_link(links,size))

print("Downloading Started...\n")
def downloader1():      
    for i in link[0]:
        try:
            yt = YouTube(i)
            ys = yt.streams.get_highest_resolution()
            filename = ys.download()
            print("threading 1 -->  " + filename.split('/')[-1] + ' Downloaded')
        except Exception as e:
            print(f"Failed to download {i}: {e}")

def downloader2():
    for i in link[1]:
        try:
            yt = YouTube(i)
            ys = yt.streams.get_highest_resolution()
            filename = ys.download()
            print("threading 1 -->  " + filename.split('/')[-1] + ' Downloaded')
        except Exception as e:
            print(f"Failed to download {i}: {e}")

def downloader3():
    for i in link[2]:
        try:
            yt = YouTube(i)
            ys = yt.streams.get_highest_resolution()
            filename = ys.download()
            print("threading 1 -->  " + filename.split('/')[-1] + ' Downloaded')
        except Exception as e:
            print(f"Failed to download {i}: {e}")

def downloader4():
    for i in link[3]:
        try:
            yt = YouTube(i)
            ys = yt.streams.get_highest_resolution()
            filename = ys.download()
            print("threading 1 -->  " + filename.split('/')[-1] + ' Downloaded')
        except Exception as e:
            print(f"Failed to download {i}: {e}")

t1 = threading.Thread(target=downloader1, name='d1')
t2 = threading.Thread(target=downloader2,name='d2')
t3 = threading.Thread(target=downloader3, name='d3')
t4 = threading.Thread(target=downloader4,name='d4')
t1.start()
t2.start()
t3.start()
t4.start()
