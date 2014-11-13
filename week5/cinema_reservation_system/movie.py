import sqlite3
from projection import Projection


class Movie:
    conn = sqlite3.connect("projections.db")
    cursor = conn.cursor()
    empty_hall = []
    row = []
    for col in range(10):
        row.append('.')
    for i in range(10):
        empty_hall.append(row)

    def __init__(self, id, name, rating):
        proj = Movie.cursor.execute("SELECT * FROM projections")
        self.id = id
        self.name = name
        self.rating = rating
        self.projections = []
        for row in proj:
            if row[1] == self.id:
                self.projections.append(Projection(row[0], row[1], row[2], row[3], row[4]))

    

