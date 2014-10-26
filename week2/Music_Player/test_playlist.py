import unittest
import song
import playlist


class PlaylistTest(unittest.TestCase):
    def setUp(self):
        self.good_playlist = playlist.Playlist("My Playlist")

    def test_playlist_init(self):
        self.assertEqual(self.good_playlist.name, "My Playlist")

    def test_add_song(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        self.good_playlist.add_song(heart_of_steel)
        self.assertEqual(len(self.good_playlist.songs), 1)

    def test_remove_song(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        self.good_playlist.songs.append(heart_of_steel)
        chandellier = song.Song("Chandellier", "Sia", "Album", 300, 128)
        self.good_playlist.songs.append(chandellier)
        self.good_playlist.remove_song("Chandellier")
        self.assertFalse(chandellier in self.good_playlist.songs)
        self.assertEqual(len(self.good_playlist.songs), 1)

    def test_total_length(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        chandellier = song.Song("Chandellier", "Sia", "Album", 300, 128)
        self.good_playlist.songs.append(heart_of_steel)
        self.good_playlist.songs.append(chandellier)
        self.assertEqual(self.good_playlist.total_length(), 700)

    def test_remove_disrated(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        chandellier = song.Song("Chandellier", "Sia", "Album", 300, 128)
        chandellier.rate(2)
        heart_of_steel.rate(5)
        self.good_playlist.songs.append(heart_of_steel)
        self.good_playlist.songs.append(chandellier)
        self.good_playlist.remove_disrated(3)
        self.assertFalse(chandellier in self.good_playlist.songs)

    def test_remove_bad_quality(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        chandellier = song.Song("Chandellier", "Sia", "Album", 300, 128)
        self.good_playlist.songs.append(heart_of_steel)
        self.good_playlist.songs.append(chandellier)
        self.good_playlist.remove_bad_quality()
        self.assertFalse(heart_of_steel in self.good_playlist.songs)

    def test_show_artists(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        chandellier = song.Song("Chandellier", "Sia", "Album", 300, 128)
        sia_song = song.Song("My Love", "Sia", "Blabla", 250, 192)
        self.good_playlist.songs.append(heart_of_steel)
        self.good_playlist.songs.append(chandellier)
        self.good_playlist.songs.append(sia_song)
        self.good_playlist.show_artists()
        self.assertEqual(self.good_playlist.show_artists(), {"Sia", "Manowar"})

    def test_str(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        chandellier = song.Song("Chandellier", "Sia", "Album", 300, 128)
        sia_song = song.Song("My Love", "Sia", "Blabla", 250, 192)
        self.good_playlist.songs.append(heart_of_steel)
        self.good_playlist.songs.append(chandellier)
        self.good_playlist.songs.append(sia_song)
        #print(self.good_playlist)

    def test_save(self):
        heart_of_steel = song.Song("Heart of Steel", "Manowar", "Best", 400, 64)
        chandellier = song.Song("Chandellier", "Sia", "Album", 300, 128)
        sia_song = song.Song("My Love", "Sia", "Blabla", 250, 192)
        self.good_playlist.songs.append(heart_of_steel)
        self.good_playlist.songs.append(chandellier)
        self.good_playlist.songs.append(sia_song)
        self.good_playlist.save("Playlist.txt")

    #def test_load(self):
        #self.good_playlist.load("Playlist.txt")






if __name__ == '__main__':
    unittest.main()