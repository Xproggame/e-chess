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
        self.count_b = 0
        self.count_n = 0
        self.avant = 0

    def mouvement(self, pion: str, couleur):
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        if couleur == 'b':
            self.avant = 1

        else:
            self.avant = -1

        if int(self.pos.position.get(self.pos_pion)[0]) + self.avant == '':
            self.list_move.append([self.avant, 0])

        self.eat.eat(str(self.list_pos_pion[0] + self.avant) + str(self.list_pos_pion[1] + 1))

        if self.eat.possibilite:
            self.list_move.append([self.avant, 1, self.eat.point])

        self.eat.eat(str(self.list_pos_pion[0] + self.avant) + str(self.list_pos_pion[1] - 1))

        if self.eat.possibilite:
            self.list_move.append([self.avant, -1, self.eat.point])

    def promotion(self, pion):

        if self.pos.case.get(pion)[0] + self.avant == 8 or self.pos.case.get(pion)[0] + self.avant == 1:

            if self.avant == 1:
                self.count_b += 1
                self.pos.case[f'r{self.count_b}'] = self.pos.case.pop(pion)
                self.pos.position[self.pos_pion] = f'r{self.count_b}'
            
            else:
                self.count_n += 1
                self.pos.case[f'r{self.count_n}'] = self.pos.case.pop(pion)
                self.pos.position[self.pos_pion] = f'r{self.count_n}'