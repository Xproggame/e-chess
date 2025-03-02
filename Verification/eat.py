from Info.Board import *
from Info.Pièce import *
from Verification.In import *


class Eat:

    def __init__(self, pos: Board, point: Piece):
        self.pos = pos
        self.pion = point
        self.possibilite = False
        self.piece = ''
        self.point = 0
        self.bloque = False
        self.pion_adverse = False

    def eat(self, case: str, couleur):
        self.pion_adverse = False

        if not out(case):

            if self.pos.position.get(case) != '' and self.pos.position.get(case).find(couleur) == -1:
                self.pion_adverse = True
                self.possibilite = True
                self.piece = self.pos.position.get(case)
                self.pion.find_point(self.piece)
                self.point = self.pion.ez_point

            elif self.pos.position.get(case).find(couleur) != -1:
                self.bloque = True

            else:
                self.possibilite = False
                self.bloque = False

    def delete(self, piece, couleur):
        remove_var = {
            'b': self.pion.piece_b.remove(self.pion),
            'n': self.pion.piece_n.remove(self.pion)
        }
        self.pos.case[piece] = False
        remove_var.get(couleur)()
