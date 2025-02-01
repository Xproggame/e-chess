from Pos import *
from Pièce import *

point = Piece()


class Eat:

    def __init__(self, pos: Position):
        self.pos = pos
        self.possibilite = False
        self.piece = ''
        self.point = 0

    def eat(self, case):

        if self.pos.position.get(case) != '':
            self.possibilite = True
            self.piece = self.pos.position.get(case)
            point.find_point(self.piece)
            self.point = point.ez_point

        else:
            self.possibilite = False

    def delete(self, piece):
        self.pos.case[piece] = False
