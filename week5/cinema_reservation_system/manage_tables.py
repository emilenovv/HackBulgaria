import sqlite3


def add_movie(new_name, new_rating):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies(name, rating) VALUES (?, ?)", (new_name, new_rating))
    conn.commit()
    conn.close()


def add_projection(movie_id, type, date, time):
    conn = sqlite3.connect("projections.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO projections(movie_id, type, date, time) VALUES (?, ?, ?, ?)",
                   (movie_id, type, date, time))
    conn.commit()
    conn.close()


def add_reservations(username, projection_id, row, col):
    conn = sqlite3.connect("reservations.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO reservations(username, projection_id, row, col) VALUES (?, ?, ?, ?)",
                   (username, projection_id, row, col))
    conn.commit()


def show_movies():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM movies")
    for row in result:
        print("[{}] - {} ({})".format(row[0], row[1], row[2]))


def show_projections(movie_id):
    conn = sqlite3.connect("projections.db")
    cursor = conn.cursor()
    result = cursor.execute("SELECT * FROM projections WHERE movie_id = ?", (movie_id, ))
    for row in result:
        print("[{}] - {} {} ({})".format(row[0], row[3], row[4], row[2]))


def show_projections_by_date(movie_id, date):
    conn = sqlite3.connect("projections.db")
    cursor = conn.cursor()
    movie = cursor.execute("SELECT  FROM projections")
    result = cursor.execute("SELECT * FROM projections WHERE movie_id = ? AND date = ?", (movie_id, date))
    print("Projections for movie {} on date {}".format(movie_id, date))
    for row in result:
        print("[{}] - {} {} ({})".format(row[0], row[3], row[4], row[2]))

def welcome():
    print("Hello! To add new movie - \"new_movie\",")
    print("to add new projection - \"new_projection\", for new reservation - \"new_reservation\"")
    print("If you want to see the movies - \"show_movies\"")
    print("To see projections = \"show_projections <movie_id>\"")
    print("To exit - type \"quit\"")


def enter_command():
    while True:
        command = input("command> ")
        if command == "new_movie":
            name = input("Please add the name of the movie: ")
            rating = input("Please add rating for the new movie: ")
            add_movie(name, float(rating))
        elif command == "new_projection":
            movie_id = input("Enter the id of the movie which is to be projected: ")
            type = input("Enter the type of the projection: ")
            date = input("Enter the date of the projection: ")
            time = input("And the time: ")
            add_projection(int(movie_id), type, date, time)
        elif command == "new_reservation":
            username = input("Enter the name to whom belong the reservation: ")
            projection_id = input("Enter the projection_id: ")
            row = input("Enter the row of the seat: ")
            col = input("And the colon: ")
            add_reservations(username, int(projection_id), int(row), int(col))
        elif command == "show_movies":
            show_movies()
        elif command.split()[0] == "show_projections":
            show_projections(int(command.split()[1]))
        elif command == "quit":
            break
        else:
            print("You have entered incorrect command.")


def main():
    welcome()
    enter_command()

if __name__ == '__main__':
    main()