import os
import random

file = open('playlist.txt', 'r').read().split('\n') 

random.shuffle(file) # Shuffle the Playlist

## Add all hyperlinks to a single string
videos = ''
for i in file:
    videos+= f"{i} "

## Run it all
os.system(f'vlc --no-video {videos}')
    

