from music_crawler import MusicCrawler
from playlist import Playlist
import unittest


class TestMusicCrawler(unittest.TestCase):
    def setUp(self):
        self.my_music_crawler = MusicCrawler("/home/emil/Downloads/Rammstein-GH.2009/CD1/")

    def test_init(self):
        self.assertEqual(self.my_music_crawler.path, "/home/emil/Downloads/Rammstein-GH.2009/CD1/")

    def test_generate_playlist_raw_format(self):
        self.my_music_crawler.generate_playlist()
        self.my_music_crawler.generated_playlist.save("emoemo.json")





if __name__ == '__main__':
    unittest.main()