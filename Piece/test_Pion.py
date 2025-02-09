from unittest import TestCase
from Pion import Pion
from Pos import Position
from Eat import Eat


class TestPion(TestCase):
    def test_mouvement(self):
        eat = Eat()
        pos = Pos()
        pion = Pion(pos, eat)
        pion.mouvement('pb8', 'b')
        self.assertEquals(pion.list_move, ['83z'])

    def test_promotion(self):
        self.fail()
