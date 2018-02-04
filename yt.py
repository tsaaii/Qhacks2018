#you need to import pytube 6.4.2


pip install pytube==6.4.2

import pytube
pytube.__version__ 

#this should give 6.4.2

from pytube import YouTube
yt=YouTube('the input video link should come here')
yt = yt.get('mp4', '360p')
yt.download('C:\\Users\\Owner\\Desktop\\324')#this is the download location
