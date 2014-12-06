from random import choice, randrange


def draw_board(board):
    line = " | "
    horizontal_lines = '-' * 11
    print(" " + board[6] + line + board[7] + line + board[8])
    print(horizontal_lines)
    print(" " + board[3] + line + board[4] + line + board[5])
    print(horizontal_lines)
    print(" " + board[0] + line + board[1] + line + board[2])


def choose_between_X_or_O():
    while True:
        symbol = input("With what do you want to play - X or O?> ").upper()
        if symbol == "X":
            return "X", "O"
        else:
            return "O", "X"
        print("Please, choose between X and O!")


def player_choose_position(board, symbol):
    print("Every field corresponds to the number on your numpad")
    while True:
        place = int(input('''Select where to put {}. > '''.format(symbol)))
        if place >= 1 and place <= 9:
            if is_place_free(board, place - 1) is True:
                actual_place = place - 1
                return actual_place
            else:
                print("This place is taken. Choose another.")
        print("Select between 1 and 9!")


def is_place_free(board, position):
    return board[position] == " "


def is_board_full(board):
    for place in board:
        if place == " ":
            return False
    return True


def choose_move_from_list(board, list):
    possible_moves = []
    for move in list:
        if is_place_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) != 0:
        return choice(possible_moves)
    return False


def computer_choose_position(board, player_symbol, num_computer_symbols):
    if player_symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"

    #proverqva dali moje da bie v slevashtiq hod
    for i in range(9):
        if is_place_free(board, i):
            board[i] = computer_symbol
            if is_winner(board, computer_symbol):
                print(i)
                board[i] = " "
                return i
            board[i] = " "

    #opitva se da blokira ako moje
    for i in range(9):
        if is_place_free(board, i):
            board[i] = player_symbol
            if is_winner(board, player_symbol):
                board[i] = " "
                return i
            board[i] = " "

    corners = [0, 2, 6, 8]
    move = choose_move_from_list(board, corners)
    if move is not False:
        return move

    #opitva se da sloji simvol v protivopolojniq ygyl
    if num_computer_symbols == 1:
        if board[0] == computer_symbol and is_place_free(board, 8):
            return 8
        elif board[8] == computer_symbol and is_place_free(board, 0):
            return 0
        elif board[2] == computer_symbol and is_place_free(board, 6):
            return 6
        elif board[6] == computer_symbol and is_place_free(board, 2):
            return 2

    if num_computer_symbols == 2:
        if board[0] == computer_symbol and board[8] == computer_symbol:
            if is_place_free(board, 6):
                return 6
            elif is_place_free(board, 2):
                return 2
        if board[6] == computer_symbol and board[2] == computer_symbol:
            if is_place_free(board, 0):
                return 0
            elif is_place_free(board, 2):
                return 2

        if is_place_free(board, 4):
            return 4

        move = choose_move_from_list(board, corners)
        if move is not False:
            return move

        sides = [1, 3, 6, 8]
        move = choose_move_from_list(board, sides)
        return move


def make_move(board, move, symbol):
    board[move] = symbol


def player_starts_first():
    random_num = randrange(2)
    if random_num == 0:
        return False
    return False


def is_winner(board, symbol):
    is_winner_flag = True
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (7, 4, 1), (8, 5, 2),
                            (0, 4, 8), (6, 4, 2)]
    for comb in winning_combinations:
        is_winner_flag = True
        for position in comb:
            if board[position] != symbol:
                is_winner_flag = False
        if is_winner_flag is True:
            print(symbol)
            print(comb)
            return True
    return False


def do_want_to_play_again():
    while True:
        answer = input("Do you wanna play again - yes or no? ")
        if answer == "yes":
            return True
        elif answer == "no":
            return False
        print("Just answer - yes or no? ")


def main():
    while True:
        board = [" "] * 9
        num_computer_symbols = 0
        player_symbol, computer_symbol = choose_between_X_or_O()
        print("Player symbol {}".format(player_symbol))
        print("Computer symbol {}".format(computer_symbol))
        player_turn = player_starts_first()
        if player_turn is True:
            print("You will go first!")
        else:
            print("Computer will go first! Good luck!")
        while True:
            if player_turn is True:
                print("Player turn")
                draw_board(board)
                move = player_choose_position(board, player_symbol)
                make_move(board, move, player_symbol)
                if is_winner(board, player_symbol):
                    draw_board(board)
                    print("You won! Congrats!")
                    break
                else:
                    if is_board_full(board) is True:
                        draw_board(board)
                        print("No one wins!")
                        break
                    else:
                        player_turn = False

            #red na kompiutyra
            else:
                print("Computer turn")
                move = computer_choose_position(board, computer_symbol, num_computer_symbols)
                print(move)
                make_move(board, move, computer_symbol)
                num_computer_symbols += 1
                if is_winner(board, computer_symbol):
                    draw_board(board)
                    print("Sorry, you lost! HAHAHAHA")
                    break
                else:
                    if is_board_full(board) is True:
                        draw_board(board)
                        print("No one wins!")
                        break
                    else:
                        player_turn = True

        if do_want_to_play_again() is False:
            break


if __name__ == '__main__':
    main()