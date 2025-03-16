import unittest
from Bot.Move import Move
from Info.Board import Board
from Piece.Pion import Pion
from Piece.Tour import Tour
from Piece.cavalier import Cavalier
from Piece.fou import Fou
from Piece.Reine import Reine
from Piece.Roi import Roi
from Verification.eat import Eat
from Info.Pièce import Piece
from Bot.Arbre import Arbre
from Info.Mouvement import Conversion


class MyTestCase(unittest.TestCase):
    def test_something(self):
        info = Piece()
        board = Board()
        convert = Conversion(board)
        eat = Eat(board, info)
        roi = Roi(board, eat)
        reine = Reine(board, eat)
        fou = Fou(board, eat)
        tour = Tour(board, eat)
        cavalier = Cavalier(board, eat)
        pion = Pion(board, eat)
        move = Move(board, pion, cavalier, fou, tour, reine, roi, eat, info)
        arbre = Arbre(move, info, board, convert)
        self.assertEqual(arbre.create_arbre('n', 'b'), ['86', 'pn8'])  # add assertion here


if __name__ == '__main__':
    unittest.main()
