import datetime
from movie import Movie
from projection import Projection
from reservation import Reservation
from sqlalchemy import func
import ast


class Cinema():

    def __init__(self, session):
        self.__session = session

    def movie_details(self):
        name = input("Enter the name of the movie: ")
        rating = input("Enter the rating of the movie: ")
        movie = (name, rating)
        return movie

    def add_movie(self):
        self.movie_tuple = self.movie_details()
        movie = Movie(name=self.movie_tuple[0], rating=self.movie_tuple[1])
        self.__session.add(movie)
        self.__session.commit()

    def show_movies(self):
        all_movies = self.__session.query(Movie).all()
        for movie in all_movies:
            print(movie)

    def obtain_date(self):
        isValid = False
        while not isValid:
            date = input("Enter the date of the projection (yyyy-mm-dd): ")
            try:
                d = datetime.datetime.strptime(date, "%Y-%m-%d")
                isValid = True
            except:
                print("Enter a valid date.")
            date_to_string = str(d).split()[0]
        return date_to_string

    def obtain_time(self):
        isValid = False
        while not isValid:
            time = input("Enter the time of the projection (hh:mm): ")
            try:
                t = datetime.datetime.strptime(time, "%H:%M")
                isValid = True
            except:
                print("Enter a valid time.")
        time_to_string = str(t).split()[1]
        return time_to_string

    def add_projection(self):
        movie_id = input("Type the movie_id: ")
        movie_name = self.get_movie_title_by_id(movie_id)
        print("Adding projection for " + movie_name)
        type = input("Enter the type of the projection: ")
        date = self.obtain_date()
        time = self.obtain_time()
        projection = Projection(type=type, date=date, time=time, movie_id=movie_id)
        self.__session.add(projection)
        self.__session.commit()

    def get_movie_title_by_id(self, movie_id):
        movie = self.__session.query(Movie).filter(
            Movie.id == movie_id).one()
        return movie.name

    def get_projections_for_a_movie(self, movie_id):
        projections = self.__session.query(
            Projection).filter(Projection.movie_id == movie_id).group_by(
            Projection.date).all()
        for projection in projections:
            print(projection)

    def show_projections_available_spots(self, movie_id):
        movie_name = self.get_movie_title_by_id(movie_id)
        print("Showing projections for " + movie_name)
        projections = self.__session.query(
            Projection).filter(Projection.movie_id == movie_id).all()
        for projection in projections:
            print(projection, ' - ', str(self.available_seats(projection.id)), "available seats")

    def available_seats(self, projection_id):
        seats = 100
        self.occupied_seats = self.__session.query(
            func.count(Reservation.id)).filter(
            Reservation.projection_id == projection_id).all()[0][0]
        self.free_seats = seats - self.occupied_seats
        return self.free_seats

    def print_seats(self):
        self.seats[0][0] = ' '
        for k in range(1, 11):
            self.seats[0][k] = str(k) + " "
        for k in range(1, 11):
            self.seats[k][0] = str(k) + " "
            if k == 10:
                self.seats[k][0] = str(k)
        for i in range(11):
            print(" ".join(str(x) for x in self.seats[i]))

    def check_seats_for_out_of_index(self, seats):
        seat = ast.literal_eval(seats)
        if seat[0] > 10 or seat[0] < 0 or seat[1] > 10 or seat[1] < 0:
            print("There is no such seat in our hall!")
            return False
        else:
            return True

    def show_seats(self, projection_id):
        seats = self.__session.query(
            Reservation.col, Reservation.row).filter(
            Reservation.projection_id == projection_id).all()
        self.seats = [[". " for x in range(11)] for x in range(11)]
        self.all_seats = []
        for seat in seats:
            self.seats[seat[0]][seat[1]] = 'X '
            self.free_seats -= 1
        self.print_seats()

    def check_seats_if_available(self, seats):
        place = ast.literal_eval(seats)
        if self.check_seats_for_out_of_index(seats) is True:
            if self.seats[place[0]][place[1]] == 'X ':
                print("This seat is taken!")
                return False
        else:
            return True

    def take_seats(self, seats, projection_id):
        place = ast.literal_eval(seats)
        if self.seats[place[0]][place[1]] == ". ":
            self.seats[place[0]][place[1]] = "X "
            self.free_seats -= 1
            self.all_seats.append(place)

    def make_reservation(self, username, projection_id, seats):
        seat = ast.literal_eval(seats)
        reservation = Reservation(
            username=username, row=seat[0],
            col=seat[1], projection_id=projection_id)
        self.__session.add(reservation)
        self.__session.commit()

    def cancel_reservation(self, username):
        self.__session.query(Reservation).filter(
            Reservation.username == username).delete()
        self.__session.commit()

    def print_reservation(self, movie_id, projection_id):
        print("This is your reservation: ")
        print("Movie")
        movie = self.__session.query(
            Movie).filter(
            Movie.id == movie_id).one()
        print(movie)
        print("Date and Time: ")
        projection = self.__session.query(
            Projection).filter(
            Projection.id == projection_id).one()
        print(projection)
        seats = " "
        for seat in self.all_seats:
            seats += str(seat)
        print("Seats: " + seats)

