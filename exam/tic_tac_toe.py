from random import choice


class TicTacToe:
    def __init__(self):
        self.board = [" "] * 9
        self.free_positions = [x for x in range(9)]

    def draw_board(self):
        line = " | "
        horizontal_lines = '-' * 11
        print(" " + self.board[6] + line + self.board[7] + line + self.board[8])
        print(horizontal_lines)
        print(" " + self.board[3] + line + self.board[4] + line + self.board[5])
        print(horizontal_lines)
        print(" " + self.board[0] + line + self.board[1] + line + self.board[2])

    def choose_between_X_or_O(self):
        while True:
            self.player_symbol = input("With what do you want to play - X or O?> ").upper()
            if self.player_symbol == "X":
                self.computer_symbol = "O"
                break
            elif self.player_symbol == "O":
                self.computer_symbol = "X"
                break
            print("Please, choose between X and O!")

    def player_choose_position(self):
        print("Every field corresponds to the number on your numpad")
        while True:
            place = int(input('''Select where to put {}. > '''.format(self.player_symbol)))
            if place >= 1 and place <= 9:
                if self.is_place_free(place - 1) is True:
                    actual_place = place - 1
                    self.free_positions.remove(actual_place)
                    return actual_place
                else:
                    print("This place is taken. Choose another.")
            print("Select between 1 and 9!")

    def is_place_free(self, position):
        return position in self.free_positions

    def is_board_full(self):
        return len(self.free_positions) == 0

    def choose_move_from_list(self, list):
        possible_moves = []
        for move in list:
            if self.is_place_free(move):
                possible_moves.append(move)

        if len(possible_moves) != 0:
            return choice(possible_moves)
        return False

    def computer_tries_to_win(self):
        for i in range(9):
            if self.is_place_free(i):
                self.board[i] = self.computer_symbol
                if self.is_winner(self.computer_symbol):
                    self.board[i] = " "
                    self.free_positions.remove(i)
                    return i
                self.board[i] = " "
        return False

    def computer_tries_to_block(self):
        for i in range(9):
            if self.is_place_free(i):
                self.board[i] = self.player_symbol
                if self.is_winner(self.player_symbol):
                    self.board[i] = " "
                    self.free_positions.remove(i)
                    return i
                self.board[i] = " "
        return False

    def computer_chooses_corner(self):
        corners = [0, 2, 6, 8]
        move = self.choose_move_from_list(corners)
        if move is not False:
            self.free_positions.remove(move)
            return move
        return False

    def computer_chooses_across_corner(self):
        if self.board[0] == self.computer_symbol and self.is_place_free(8):
            self.free_positions.remove(8)
            return 8
        elif self.board[8] == self.computer_symbol and self.is_place_free(0):
            self.free_positions.remove(0)
            return 0
        elif self.board[2] == self.computer_symbol and self.is_place_free(6):
            self.free_positions.remove(6)
            return 6
        elif self.board[6] == self.computer_symbol and self.is_place_free(2):
            self.free_positions.remove(2)
            return 2
        return False

    def computer_chooses_third_corner(self):
        if self.board[0] == self.computer_symbol and self.board[8] == self.computer_symbol:
            if self.is_place_free(6):
                self.free_positions.remove(6)
                return 6
            elif self.is_place_free(2):
                self.free_positions.remove(2)
                return 2
        elif self.board[6] == self.computer_symbol and self.board[2] == self.computer_symbol:
            if self.is_place_free(0):
                self.free_positions.remove(0)
                return 0
            elif self.is_place_free(8):
                self.free_positions.remove(8)
                return 2
        return False

    def computer_chooses_center(self):
        if self.is_place_free(4):
            self.free_positions.remove(4)
            return 4
        return False

    def computer_chooses_side(self):
        sides = [1, 3, 5, 7]
        move = self.choose_move_from_list(sides)
        self.free_positions.remove(move)
        return move

    def computer_choose_position(self, num_computer_symbols):
        move = self.computer_tries_to_win()
        if move is not False:
            return move
        move = self.computer_tries_to_block()
        if move is not False:
            return move
        move = self.computer_chooses_corner()
        if move is not False:
            return move
        move = self.computer_chooses_across_corner()
        if num_computer_symbols == 1 and move is not False:
            return move
        move = self.computer_chooses_third_corner()
        if num_computer_symbols == 2 and move is not False:
            return move
        move = self.computer_chooses_center()
        if move is not False:
            return move
        else:
            return self.computer_chooses_side()

    def make_move(self, move, symbol):
        self.board[move] = symbol

    def is_winner(self, symbol):
        is_winner_flag = True
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (7, 4, 1), (8, 5, 2),
                                (0, 4, 8), (6, 4, 2)]
        for comb in winning_combinations:
            is_winner_flag = True
            for position in comb:
                if self.board[position] != symbol:
                    is_winner_flag = False
            if is_winner_flag is True:
                return True
        return False

    def do_want_to_play_again(self):
        while True:
            answer = input("Do you wanna play again - yes or no? ")
            if answer == "yes":
                return True
            elif answer == "no":
                return False
            print("Just answer - yes or no? ")


def main():
    while True:
        tictactoe = TicTacToe()
        num_computer_symbols = 0
        tictactoe.choose_between_X_or_O()
        print("You will go first!")
        player_turn = True
        while True:
            print(tictactoe.free_positions)
            if player_turn is True:
                print("Player turn")
                tictactoe.draw_board()
                move = tictactoe.player_choose_position()
                tictactoe.make_move(move, tictactoe.player_symbol)
                if tictactoe.is_winner(tictactoe.player_symbol):
                    tictactoe.draw_board()
                    print("You won! Congrats!")
                    break
                else:
                    if tictactoe.is_board_full() is True:
                        tictactoe.draw_board()
                        print("No one wins!")
                        break
                    else:
                        player_turn = False

            #red na kompiutyra
            else:
                print("Computer turn")
                move = tictactoe.computer_choose_position(num_computer_symbols)
                tictactoe.make_move(move, tictactoe.computer_symbol)
                num_computer_symbols += 1
                if tictactoe.is_winner(tictactoe.computer_symbol):
                    tictactoe.draw_board()
                    print("Sorry, you lost! HAHAHAHA")
                    break
                else:
                    if tictactoe.is_board_full() is True:
                        tictactoe.draw_board()
                        print("No one wins!")
                        break
                    else:
                        player_turn = True

        if tictactoe.do_want_to_play_again() is False:
            break


if __name__ == '__main__':
    main()
