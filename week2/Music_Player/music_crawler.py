import glob
from playlist import Playlist
from song import Song
from mutagen.mp3 import MP3


class MusicCrawler:
    def __init__(self, path):
        self.path = path
        self.generated_playlist = Playlist("")

    def get_raw_playlist(self):
        raw_playlist = glob.glob(self.path + "*.mp3")
        return raw_playlist

    def generate_playlist(self):
        self.generated_playlist.name = "No Name"
        raw_playlist = self.get_raw_playlist()
        mutagen_playlist = []
        for song in raw_playlist:
            mutagen_playlist.append(MP3(song))
        for index in range(len(mutagen_playlist)):
            title = mutagen_playlist[index]["TIT2"]
            artist = mutagen_playlist[index]["TPE2"]
            album = str(mutagen_playlist[index]["TALB"])
            length = mutagen_playlist[index].info.length
            bitrate = mutagen_playlist[index].info.bitrate
            self.generated_playlist.songs.append(Song(title, artist, album, length, bitrate))
        return self.generated_playlist