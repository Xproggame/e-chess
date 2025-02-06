from Info.Pos import *
from Info.Pièce import *

point = Piece()


class Eat:

    def __init__(self, pos: Position):
        self.pos = pos
        self.possibilite = False
        self.piece = ''
        self.point = 0
        self.bloque = False

    def eat(self, case: str, couleur):

        if self.pos.position.get(case) != '' and self.pos.position.get(case).find(couleur) == -1:
            self.possibilite = True
            self.piece = self.pos.position.get(case)
            point.find_point(self.piece)
            self.point = point.ez_point

        elif self.pos.position.get(case).find(couleur) != -1:
            self.bloque = True

        else:
            self.possibilite = False
            self.bloque = False

    def delete(self, piece):
        self.pos.case[piece] = False
