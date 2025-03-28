import unittest
from Piece.Reine import Reine
from test_board.test_reine import Board
from Verification.eat import Eat
from Info.Pièce import Piece

board = Board()
piece = Piece()
eat = Eat(board, piece)
reine = Reine(board, eat)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        reine.mouvement('rb', 'b')
        self.assertEqual(reine.list_move, [['52', 0], ['63', 0], ['74', 0], ['85', 0], ['42', 0], ['43', 0]])  # add assertion here


if __name__ == '__main__':
    unittest.main()
