class Song:
    def __init__(self, title, artist, album, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = 0
        self.length = length
        self.bitrate = bitrate

    def rate(self, rating):
        if rating in range(0, 6):
            self.rating = rating
        else:
            raise ValueError("Your rating must be between 0 and 5")


    
