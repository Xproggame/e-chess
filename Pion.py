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
        self.list_pos = []

    def mouvement(self, pion: str, couleur):
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])

        if couleur == 'b':
            avant = 1

        else:
            avant = -1

        if int(self.pos.position.get(self.pos_pion)[0]) + avant == '':
            self.move.position(0, avant, pion)
