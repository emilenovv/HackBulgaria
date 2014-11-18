import sqlite3


class Projection:
    conn = sqlite3.connect('reservations.db')
    cursor = conn.cursor()

    def __init__(self, id=0, movie_id=0, type=0, date=0, time=0):
        empty_hall = []
        rows = []
        for col in range(1, 11):
            rows.append([])
        for row in rows:
            for i in range(10):
                row.append('.')
        empty_hall = rows
        self.id = id
        self.movie_id = movie_id
        self.type = type
        self.date = date
        self.time = time
        self.seats = empty_hall
        self.available_seats = 100

    def show_seats(self):
        ix = 1
        col_index = "  1 2 3 4 5 6 7 8 9 10"
        print(col_index)
        for row in self.seats:
            print(ix, ' '.join(''.join(row)))
            ix += 1

    def load_reservations(self, id):
        result = Projection.cursor.execute("SELECT row, col FROM reservations WHERE projection_id = ?", (id, ))
        for row in result:
            self.seats[row[0] - 1][row[1] - 1] = "X"
            self.available_seats -= 1
