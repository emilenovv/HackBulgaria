from tic_tac_toe import TicTacToe
import unittest


class TicTacToeTests(unittest.TestCase):
    def setUp(self):
        self.tic = TicTacToe()

    def test_is_winner(self):
        self.tic.board[6] = 'X'
        self.tic.board[7] = 'X'
        self.tic.board[8] = 'X'
        self.assertTrue(self.tic.is_winner('X'))

    def test_is_winning(self):
        self.tic.board[3] = 'O'
        self.tic.board[4] = 'X'
        self.tic.board[5] = 'X'
        self.assertFalse(self.tic.is_winner('O'))

    def test_try_to_win_successfully(self):
        self.tic.computer_symbol = "O"
        self.tic.player_symbol = "X"
        self.tic.board[0] = 'X'
        self.tic.board[1] = ' '
        self.tic.board[2] = 'O'
        self.tic.board[3] = ' '
        self.tic.board[4] = 'X'
        self.tic.board[5] = 'X'
        self.tic.board[6] = 'O'
        self.tic.board[7] = ' '
        self.tic.board[8] = 'O'
        self.tic.free_positions = [1, 3, 7]
        self.assertEqual(self.tic.computer_choose_position(3), 7)

    def test_config(self):
        self.tic.computer_symbol = "O"
        self.tic.player_symbol = "X"
        self.tic.board[0] = 'X'
        self.tic.board[1] = ' '
        self.tic.board[2] = 'O'
        self.tic.board[3] = 'O'
        self.tic.board[4] = 'X'
        self.tic.board[5] = 'X'
        self.tic.board[6] = ' '
        self.tic.board[7] = ' '
        self.tic.board[8] = 'O'
        self.tic.free_positions = [1, 6, 7]
        self.tic.make_move(7, 'X')
        self.assertEqual(self.tic.computer_choose_position(3), 6)

    def test_computer_block_player(self):
        self.tic.computer_symbol = "O"
        self.tic.player_symbol = "X"
        self.tic.board[0] = 'X'
        self.tic.board[1] = ' '
        self.tic.board[2] = ' '
        self.tic.board[3] = 'O'
        self.tic.board[4] = 'X'
        self.tic.free_positions = [1, 5, 6, 7, 8]
        self.assertEqual(self.tic.computer_choose_position(1), 8)

    def test_computer_chooses_corner(self):
        self.tic.computer_symbol = "O"
        self.tic.player_symbol = "X"
        self.tic.board[4] = 'X'
        move = self.tic.computer_choose_position(1)
        self.tic.free_positions = [0, 1, 2, 3, 5, 6, 7, 8]
        corners = [0, 2, 6, 8]
        self.assertIn(move, corners)



if __name__ == '__main__':
    unittest.main()