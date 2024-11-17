from pytube import YouTube
from rich import print


class Ytdl:
    def __init__(self, url):
        self.yt = YouTube(url)
        print(self.yt.title)

    def Highest_resolution(self):
        stream = self.yt.streams.get_highest_resolution()
        stream.download()

    def Lowest_resolution(self):
        stream = self.yt.streams.get_lowest_resolution()
        stream.download()

    def Audio_only(self):
        stream = self.yt.streams.get_audio_only()
        stream.download()
