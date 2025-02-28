from unittest import TestCase
from Piece.Pion import *
from Info.Pos import Position
from Verification.eat import Eat


class TestPion(TestCase):
    def test_mouvement(self):
        pos = Position()
        eat = Eat(pos)
        pion = Pion(pos, eat)
        pion.mouvement('pb8', 'b')
        self.assertEqual(pion.list_move, [['83'], ['84']])

    def test_promotion(self):
        self.fail()
