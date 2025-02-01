from In import *
from Mouvement import *
from eat import *

out = In()


class Pion:

    def __init__(self, pos: Position, move: Conversion, eat: Eat):
        self.eat = eat
        self.pos = pos
        self.move = move
        self.pos_pion = ''
        self.list_pos_pion = []
        self.list_move = []

    def mouvement(self, pion: str, couleur):
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        if couleur == 'b':
            avant = 1

        else:
            avant = -1

        if int(self.pos.position.get(self.pos_pion)[0]) + avant == '':
            self.list_move.append([avant, 0])

        self.eat.eat(str(self.list_pos_pion[0] + avant) + str(self.list_pos_pion[1] + 1))

        if self.eat.possibilite:
            self.list_move.append([avant, 1, self.eat.point])

        self.eat.eat(str(self.list_pos_pion[0] + avant) + str(self.list_pos_pion[1] - 1))

        if self.eat.possibilite:
            self.list_move.append([avant, -1, self.eat.point])