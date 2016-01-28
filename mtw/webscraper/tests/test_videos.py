import unittest
from mtw.webscraper import videos


class TestVideos(unittest.TestCase):

    def test_find_movie(self):
        url = "http://alltube.tv/film/miasteczko-south-park-south-park-bigger-longer-uncut-1999-lektor/5330"
        print(videos.find_movie(url))


if __name__ == "__main__":
    unittest.main()