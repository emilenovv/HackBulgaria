from song import Song
import json


class Playlist:
    LOW_BITRATE = 127

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        for song in self.songs:
            if song.title == song_name:
                self.songs.remove(song)

    def total_length(self):
        result = 0
        for song in self.songs:
            result += song.length
        return result

    def remove_disrated(self, rate):
        self.songs = list(filter(lambda song: song.rating > rate, self.songs))
        return self.songs

    def remove_bad_quality(self):
        self.songs = list(filter(lambda song: song.bitrate > self.LOW_BITRATE, self.songs))
        return self.songs

    def show_artists(self):
        list_of_artists = []
        for song in self.songs:
            list_of_artists.append(song.artist)
        return set(list_of_artists)

    def __str__(self):
        str_list = []
        for index, song in enumerate(self.songs):
            minutes = int(song.length // 60)
            seconds = int(song.length % 60)
            str_list.append("[" + str(index + 1) + "] {} {} - {}:{}".format(song.artist, song.title, minutes, seconds))
        return "\n".join(str_list)

    def save(self, file_path):
        output = open(file_path, "w")
        list_of_songs = []
        for song in self.songs:
            song.__dict__["title"] = str(song.title)
            song.__dict__["artist"] = str(song.artist)
            list_of_songs.append(song.__dict__)
        output.write(json.dumps({
            "Name": self.name,
            "Songs": list_of_songs}
            , indent=4, sort_keys=True))
        output.close()

    @staticmethod
    def load(file_path):
        source = open(file_path, "r")
        data = json.load(source)
        loaded_playlist = Playlist(data["Name"])
        print(loaded_playlist.name)
        for song in range(len(data["Songs"])):
            album = data['Songs'][song]["album"]
            artist = data['Songs'][song]["artist"]
            bitrate = data['Songs'][song]["bitrate"]
            length = data['Songs'][song]["length"]
            rating = data['Songs'][song]["rating"]
            title = data['Songs'][song]["title"]
            loaded_playlist.songs.append(Song(title, artist, album, length, bitrate))
        source.close()
        return loaded_playlist

