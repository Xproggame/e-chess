from unittest import TestCase
from Piece.fou import Fou
from Info.Pos import Position
from Verification.eat import Eat


class TestPion(TestCase):
    def test_mouvement(self):
        pos = Position()
        eat = Eat(pos)
        pion = Fou(pos, eat)
        pion.mouvement('fb1', 'b')
        self.assertEqual(pion.list_move, [])

    def test_promotion(self):
        self.fail()
