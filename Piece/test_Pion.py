from unittest import TestCase
from Piece.Reine import Reine
from Info.Pos import Position
from Verification.eat import Eat


class TestPion(TestCase):
    def test_mouvement(self):
        pos = Position()
        eat = Eat(pos)
        pion = Reine(pos, eat)
        pion.mouvement('rb', 'b')
        self.assertEqual(pion.list_move, [['52']])

    def test_promotion(self):
        self.fail()
