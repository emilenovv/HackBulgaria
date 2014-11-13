class Projection:
    empty_hall = []
    row = []
    for col in range(10):
        row.append('.')
    for i in range(10):
        empty_hall.append(str(i))
        empty_hall.append(row)

    def __init__(self, id=0, movie_id=0, type=0, date=0, time=0):
        self.id = id
        self.movie_id = movie_id
        self.type = type
        self.date = date
        self.time = time
        self.seats = Projection.empty_hall
        self.available_seats = 100

    def show_seats(self):
        for row in self.seats:
            print(' '.join(''.join(row)))
