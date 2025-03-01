from Info.Board import *
from Info.Pièce import *
from Verification.In import *


class Eat:

    def __init__(self, pos: Board, point: Piece):
        self.pos = pos
        self.possibilite = False
        self.piece = ''
        self.point = 0
        self.bloque = False
        self.pion_adverse = False
        self.remove_var = {
            'b': point.piece_b.remove(piece),
            'n': point.piece_n.remove(piece)
        }

    def eat(self, case: str, couleur):
        self.pion_adverse = False

        if not out(case):

            if self.pos.position.get(case) != '' and self.pos.position.get(case).find(couleur) == -1:
                self.pion_adverse = True
                self.possibilite = True
                self.piece = self.pos.position.get(case)
                point.find_point(self.piece)
                self.point = point.ez_point

            elif self.pos.position.get(case).find(couleur) != -1:
                self.bloque = True

            else:
                self.possibilite = False
                self.bloque = False

    def delete(self, piece, couleur):
        self.pos.case[piece] = False
        self.var.get(couleur)()
