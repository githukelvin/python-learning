from pytube import Playlist,YouTube
import pandas as pd
import pafy as pf

video = yt.streams.filter(only_audio=True).first()

link = input("Input the link Of the playlist :=")

pls = Playlist(link)

Vlinks = YouTube(link).title


for url in pls:
    print(url)

    print(f"Downloading Audio of : {YouTube.url.title} ")

    try:
        # Passing link to pafy
        video = pf.new(url)

        # Extracting the best availble audio

        best_audio = video.getbestaudio()

        # Downloading
        best_audio.download()
    except Exception as e:
        print(e)
        print("Sorry, there is some error")
        print("Please try again later")
        exit()
