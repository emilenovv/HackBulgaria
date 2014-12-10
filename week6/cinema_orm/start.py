from sqlalchemy import create_engine
from cinema import Cinema
from sqlalchemy.orm import Session
from base import Base


def main():
    engine = create_engine("sqlite:///EmilCinema.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    EmilCinema = Cinema(session)
    print_main_menu()
    print("asda")
    command = input("Enter your choice: ")
    parsed_command = command.split()
    while parsed_command[0] != "end":
        if parsed_command[0] == "add_movie" or parsed_command[0] == '1':
            EmilCinema.add_movie()
        if parsed_command[0] == "show_movies" or parsed_command[0] == '2':
            EmilCinema.show_movies()
        if parsed_command[0] == "add_projection" or parsed_command[0] == '3':
            EmilCinema.add_projection()
        if parsed_command[0] == "show_movie_projections" or parsed_command[0] == '4':
            EmilCinema.show_projections_available_spots(parsed_command[1])
        if parsed_command[0] == "make_reservation" or parsed_command[0] == '5':

            try:
                user_info = personal_info(EmilCinema)
                movie_id = choosing_movie(EmilCinema)
                projection_id = choosing_projection(EmilCinema)
                choosing_seats(EmilCinema, user_info, projection_id, movie_id)
                finalize_reservation(EmilCinema, user_info, projection_id)

            except GiveUpError:
                print("You just give up the reservation!")
                print_main_menu()
            if parsed_command[0] == "cancel_reservation":
                EmilCinema.cancel_reservation(parsed_command[1])
            if parsed_command[0] == "exit":
                break
            if parsed_command[0] == "help":
                EmilCinema.print_main_menu()
        command = input("Enter your choice: ")
        parsed_command = command.split()


def personal_info(EmilCinema):
    username = input("Step 1 (User): Choose name> ")
    number_of_tickets = input("Step 1 (User): Choose number of tickets> ")
    EmilCinema.show_movies()
    return username, number_of_tickets


def choosing_movie(EmilCinema):
    movie_id = input("Step 2 (Movie): Choose a movie (type its id)> ")
    EmilCinema.show_projections_available_spots(movie_id)
    return movie_id


def choosing_projection(EmilCinema):
    projection_id = input("Step 3 (Projection): Choose a projection> ")
    print("Available seats (marked with a dot): ")
    EmilCinema.show_seats(projection_id)
    return projection_id


def choosing_seats(EmilCinema, user_info, projection_id, movie_id):
    for ticket in range(1, int(user_info[1]) + 1):
        user_seat = input("Step 4 (Seats): Choose seat {} (row, column)> ".format(ticket))
        while EmilCinema.check_seats_for_out_of_index(
                user_seat) is False or EmilCinema.check_seats_if_available(user_seat) is False:
            user_seat = input("Step 4 (Seats): Choose seat {} (row, column)> ".format(ticket))
        EmilCinema.take_seats(user_seat, projection_id)
    EmilCinema.print_reservation(movie_id, projection_id)


def finalize_reservation(EmilCinema, user_info, projection_id):
    final_command = input("Step 5 (Confirm - type 'finalize') > ")
    for seat in EmilCinema.all_seats:
        EmilCinema.make_reservation(
            final_command,
            user_info[0],
            projection_id,
            str(seat))


def print_main_menu():
    main_menu = [
        "Welcome to EmilCinema 2014!\n",
        "Here you can choose the following commands:\n",
        "1. add_movie\n",
        "2. show_movies\n"
        "3. add_projection\n",
        "4. show_movie_projections <movie_id>\n",
        "5. make_reservation\n",
        "6. cancel_reservation <name>\n",
        "7. exit\n",
        "8. help"]
    print("".join(main_menu))


class GiveUpError(Exception):
    pass


def give_up_command(command):
    if command == 'give up' or command == 'yes':
        raise GiveUpError

if __name__ == '__main__':
    main()