from movie import Movie
from projection import Projection
import sqlite3
import manage_tables


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
        while True:
            name = input("Step 1 (User) Choose name> ")
            if name == "give_up":
                break
            num_tickets = input("Step 1 (User) Choose the number of tickets> ")
            if num_tickets == "give_up":
                break
            num_tickets = int(num_tickets)
            print("Current movies:")
            self.show_movies()
            chosen_movie = None
            chosen_proj = Projection()
            movie_id = input("Step 2 (Movie) Choose a movie> ")
            if movie_id == "give_up":
                break
            movie_id = int(movie_id)
            chosen_movie = self.find_movie(movie_id)
            for projection in chosen_movie.projections:
                projection.load_reservations(projection.id)
            print("Projections for movie {}".format(chosen_movie.name))
            self.show_projection(movie_id)
            proj_id = input("Step 3 (Projection) Choose projection> ")
            if proj_id == "give_up":
                break
            proj_id = int(proj_id)
            print("Available seats (marked with a dot):")
            chosen_proj = self.find_projection(proj_id, movie_id)
            print(chosen_proj.id)
            chosen_proj.show_seats()
            seats = []
            seats = self.choose_seats(num_tickets, chosen_proj)
            if seats is False:
                break
            chosen_proj.show_seats()
            self.print_reservation_details(chosen_movie, chosen_proj, seats)
            command = input("To finalize type <finalize>: ")
            if command == "finalize":
                for seat in seats:
                    manage_tables.add_reservations(name, chosen_proj.id, seat[0], seat[1])

    def choose_seats(self, num_tickets, chosen_proj):
        seats = []
        for i in range(num_tickets):
            while True:
                seat = input("Step 4 (Seats): Choose seat {} <row> <col>> ".format(str(int(i) + 1)))
                if seat == "give_up":
                    return False
                seat = self.parse_seat(seat)
                if self.seat_in_hall(seat) is True and self.seat_is_free(seat, chosen_proj) is True:
                    break
                if self.seat_in_hall(seat) is not True:
                    print(self.seat_in_hall(seat))
                elif self.seat_is_free(seat, chosen_proj) is not True:
                    print(self.seat_is_free(seat, chosen_proj))
            self.book_seat(seat, chosen_proj)
            seats.append(seat)
        return seats

    def print_reservation_details(self, movie, projection, seats):
        print("This is your reservation:")
        print("Movie: {} ({})".format(movie.name, movie.rating))
        print("Date and Time: {} {} ({})".format(projection.date, projection.time, projection.type))
        print("Seats:")
        for seat in seats:
            print("({}, {})".format(seat[0], seat[1]))

    def find_movie(self, movie_id):
        chosen_movie = None
        for movie in self.movies:
            if movie.id == movie_id:
                chosen_movie = movie
        return chosen_movie

    def find_projection(self, proj_id, movie_id):
        chosen_proj = Projection()
        chosen_movie = self.find_movie(movie_id)
        for projection in chosen_movie.projections:
            if projection.id == proj_id:
                chosen_proj = projection
        return chosen_proj

    def parse_seat(self, seat):
        seat = seat.split()
        seat_tuple = tuple(map(int, seat))
        return seat_tuple

    def book_seat(self, seat, projection):
        row = seat[0] - 1
        col = seat[1] - 1
        if self.seat_can_be_booked(seat, projection):
            projection.seats[row][col] = 'X'
            projection.available_seats -= 1
            return True

    def seat_in_hall(self, seat):
        if seat[0] in range(1, 11) and seat[1] in range(1, 11):
            return True
        return "There is no such seat in the hall."

    def seat_is_free(self, seat, projection):
        row = seat[0] - 1
        col = seat[1] - 1
        if projection.seats[row][col] == '.':
            return True
        return "This seat is already taken."

    def seat_can_be_booked(self, seat, projection):
        if self.seat_in_hall(seat):
            if self.seat_is_free(seat, projection):
                return True
        return False

    def show_help(self):
        help_menu = ["Type \'make_reservation\' to make a reservation,",
                     " \'cancel_reservation\'' <name> to cancel a reservation ",
                     "or \'exit\' - to exit the program."]
        print(''.join(help_menu))

    def cancel_reservation(self, name):
        conn = sqlite3.connect("reservations.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM reservations WHERE username = ?", (name, ))
        conn.commit()

    def welcome_screen(self):
        print("Welcome to your cinema reservation system.")
        print("To see your options - type \'help\'")

    def choose(self):
        self.welcome_screen()
        while True:
            command = input("command> ")
            if command == "help":
                self.show_help()
            elif command == "make_reservation":
                self.make_reservation()
            elif command.split()[0] == "cancel_reservation":
                name = self.parse_cancel_reservation_command(command)
                self.cancel_reservation(name)
            elif command == "exit":
                break
            else:
                print("Unknown command. Type \'help\' to see the help menu.")
        print("Goodbye!")

    def parse_cancel_reservation_command(self, command):
        command = command.split()
        command.remove("cancel_reservation")
        command = ' '.join(command)
        return command


def main():
    cinema = Cinema()
    cinema.choose()

if __name__ == '__main__':
    main()
