import song
import unittest

class SongTest(unittest.TestCase):
    def setUp(self):
        self.my_song = song.Song("Chandellier", "Sia", "Album", 300, 128)

    def test_song_init(self):
        self.assertEqual(self.my_song.artist, "Sia")
        self.assertEqual(self.my_song.title, "Chandellier")
        self.assertEqual(self.my_song.album, "Album")
        self.assertEqual(self.my_song.rating, 0)
        self.assertEqual(self.my_song.length, 300)
        self.assertEqual(self.my_song.bitrate, 128)

    def test_rate_song(self):
        self.my_song.rate(5)
        self.assertEqual(self.my_song.rating, 5)

    def test_rate_out_of_bounds(self):
        with self.assertRaises(ValueError):
            self.assertEqual(self.my_song.rate(6), "Your rating must be between 0 and 5")

    


if __name__ == '__main__':
    unittest.main()