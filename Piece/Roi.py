from Verification.In import *
from Verification.eat import *


class Roi:

    def __init__(self, pos: Position, eat: Eat, out: In):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_possible = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        self.list_pos_pion = []
        self.pos_pion = ''

    def mouvement(self, pion, couleur):
        self.list_move = []
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        for element in self.list_possible:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])