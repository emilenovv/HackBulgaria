from music_crawler import MusicCrawler
from playlist import Playlist
import pygame


class MusicPlayer:
    def __init__(self):
        self.playlist = Playlist("Current playing")

    def welcome(self):
        print("Welcome to Emil Velikov's player!")
        print("You can choose between the following commands:")
        print("1. play from <path> - Play music from particular directory")
        print("2. load from <path> - Load your custom playlist.")
        print("3. save to <path> - Save your playlist.")
        print("4. exit - Exit")

    def play(self, file_path):
        print("Enter \"stop\" to stop the current song or \"back\" to return to previous menu")
        while True:
            print("Now playing " + file_path.split('/')[len(file_path.split('/')) - 1])
            choise = input("Enter command: ")
            if choise == "play":
                pygame.init()
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
            if choise == "stop":
                pygame.mixer.music.stop()
            elif choise == "back":
                print("You went to the previous menu. If you want to see the songs againt type \"list\"")
                return True
            else:
                print("Please choose between \"play\", \" stop\" and \"back\"")

    def make_choice(self):
        self.welcome()
        while True:
            choise = input("Enter command: ")
            if choise.split()[0] == "play" and choise.split()[1] == "from":
                current_crawler = MusicCrawler(choise.split()[2])
                current_playlist = MusicCrawler(choise.split()[2]).generate_playlist()
                for song in current_playlist.songs:
                    self.playlist.songs.append(song)
                print(self.playlist)
                num_song = input("Enter the number of the song you want to play: ")
                print()
                song_to_play = current_crawler.get_raw_playlist()[int(num_song) - 1]
                self.play(song_to_play)
            elif choise == "list":
                print(self.playlist)
            elif choise == "exit":
                break
            elif choise.split()[0] == "save" and choise.split()[1] == "to":
                Playlist("New Playlist").save(choise.split()[2])





def main():
    mp = MusicPlayer()
    mp.make_choice()

if __name__ == '__main__':
    main()