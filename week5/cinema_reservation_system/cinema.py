from movie import Movie
from projection import Projection
import sqlite3


class Cinema:
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM movies ORDER BY rating DESC")

    def __init__(self):
        self.movies = []
        for row in Cinema.result:
            self.movies.append(Movie(row[0], row[1], row[2]))

    def show_movies(self):
        for movie in self.movies:
            print("[{}] - {} ({})".format(movie.id, movie.name, movie.rating))

    def show_projection(self, movie_id):
        for movie in self.movies:
            if movie.id == movie_id:
                for projection in movie.projections:
                    print("[{}] - {} {} ({}) - {} available seats.".format(projection.id, projection.date,
                          projection.time, projection.type, projection.available_seats))

    def show_projection_by_date(self, movie_id, date):
        current_movie = ""
        for movie in self.movies:
            if movie.id == movie_id:
                current_movie = movie.name
                for projection in movie.projections:
                    if date == projection.date:
                        print("[{}] - {} ({})".format(projection.id, projection.time, projection.type))
        print("Projections for the film {} on date {}".format(current_movie, date))

    def make_reservation(self):
        # name = input("Step 1 (User) Choose name> ")
        # num_tickets = input("Step 1 (User) Choose the number of tickets> ")
        # print("Current movies:")
        # self.show_movies()
        chosen_movie = None
        chosen_proj = Projection()
        movie_id = int(input("Step 2 (Movie) Choose a movie> "))
        for movie in self.movies:
            if movie.id == movie_id:
                chosen_movie = movie
                print("Projections for movie {}".format(movie.name))
        self.show_projection(movie_id)
        proj_id = input("Step 3 (Projection) Choose projection> ")
        print("Available seats (marked with a dot):")
        for projection in chosen_movie.projections:
            if projection.id == proj_id:
                chosen_proj = projection
        chosen_proj.show_seats()





c = Cinema()
c.make_reservation()