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
print("Choose resolution to download.\n1. 480p\n2. 720p\n3. 1080p\n4. 4k")
choice = input("Select resolution: ")
if choice == '1':
    res = "480p"
elif choice == '2':
    res = "720p"
elif choice == '3':
    res = "1080p"
elif choice == '4':
    res = "2160p"
else:
    print("Choose correct resolution.")
    sys.exit(0)

print("\nPlaylist Name : {}\nChannel Name  : {}\nTotal Videos  : {}\nTotal Views   : {}".format(p.title,p.owner,p.length,p.views))
links = []
size = 0
try:
    for url in p.video_urls:
        links.append(url)
except:
    print('Playlist link is not valid.')
    sys.exit(0)
    
def split(links,size):
    for i in range(0,len(links),size):
        yield links[i:i+size]
      
size = ceil(len(links)/4)
link = list(split(links,size))

print("Downloading Started...\n")
def downloader1():
    for i in link[0]:
      yt = YouTube(i)
      for j in yt.streams:
          check_res = str(j)
          if  check_res.find(res) > 0:
              ys = yt.streams.filter(res=res).first()
              break
          else:
              ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 1 -->  " + filename.split('/')[-1] + ' -> Downloaded')

def downloader2():
    for i in link[1]:
      yt = YouTube(i)
      for j in yt.streams:
          check_res = str(j)
          if check_res.find(res) > 0:
              ys = yt.streams.filter(res=res).first()
              break
          else:
              ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 2 -->  " + filename.split('/')[-1] + ' -> Downloaded')

def downloader3():
    for i in link[2]:
      yt = YouTube(i)
      for j in yt.streams:
          check_res = str(j)
          if check_res.find(res) > 0:
              ys = yt.streams.filter(res=res).first()
              break
          else:
              ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 3 -->  " + filename.split('/')[-1] + ' -> Downloaded')

def downloader4():
    for i in link[3]:
      yt = YouTube(i)
      for j in yt.streams:
          check_res = str(j)
          if check_res.find(res) > 0:
              ys = yt.streams.filter(res=res).first()
              break
          else:
              ys = yt.streams.get_highest_resolution()
      filename = ys.download()
      print("threading 4 -->  " + filename.split('/')[-1] + ' -> Downloaded')

t1 = threading.Thread(target=downloader1, name='d1')
t2 = threading.Thread(target=downloader2,name='d2')
t3 = threading.Thread(target=downloader3, name='d3')
t4 = threading.Thread(target=downloader4,name='d4')
t1.start()
t2.start()
t3.start()
t4.start()
