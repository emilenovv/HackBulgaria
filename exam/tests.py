import tic_tac_toe
import unittest


class TicTacToeTests(unittest.TestCase):
    def setUp(self):
        self.board = [" "] * 9

    def test_is_winner(self):
        self.board[6] = 'X'
        self.board[4] = 'X'
        self.board[2] = 'X'
        self.assertTrue(tic_tac_toe.is_winner(self.board, 'X'))

    def test_win_successfully(self):
        self.board[0] = 'X'
        self.board[1] = ' '
        self.board[2] = 'O'
        self.board[3] = ' '
        self.board[4] = 'X'
        self.board[5] = 'X'
        self.board[6] = 'O'
        self.board[7] = ' '
        self.board[8] = 'O'
        print()
        tic_tac_toe.draw_board(self.board)
        self.assertEqual(tic_tac_toe.computer_choose_position(self.board, 'O', 4), 7)




if __name__ == '__main__':
    unittest.main()