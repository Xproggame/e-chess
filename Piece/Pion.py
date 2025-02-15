from Verification.eat import *


class Pion:

    def __init__(self, pos: Position, eat: Eat):
        self.eat = eat
        self.pos = pos
        self.pos_pion = ''
        self.list_pos_pion = []
        self.list_move = []
        self.count_b = 0
        self.count_n = 0
        self.avant = 0

    def mouvement(self, pion: str, couleur):
        self.list_move = []
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        if couleur == 'b':
            self.avant = 1

        else:
            self.avant = -1

        pos = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1] + self.avant)
        self.eat.eat(pos, couleur)

        if not self.eat.bloque:

            if not self.eat.pion_adverse:
                self.list_move.append(pos)

        pos = str(self.pos.case.get(pion)[0] + 1) + str(self.pos.case.get(pion)[1] + self.avant)
        self.eat.eat(pos, couleur)

        if self.eat.possibilite:

            if not out(pos):
                self.list_move.append([pos, self.eat.point])

        pos = str(self.pos.case.get(pion)[0] - 1) + str(self.pos.case.get(pion)[1] + self.avant)
        self.eat.eat(pos, couleur)

        if self.eat.possibilite:

            if not out(pos):
                self.list_move.append([pos, self.eat.point])

    def promotion(self, pion):

        if self.pos.case.get(pion)[0] + self.avant == 8 or self.pos.case.get(pion)[0] + self.avant == 1:

            if self.avant == 1:
                self.count_b += 1
                self.pos.case[f'r{self.count_b}'] = self.pos.case.pop(pion)
                self.pos.position[self.pos_pion] = f'r{self.count_b}b'
            
            else:
                self.count_n += 1
                self.pos.case[f'r{self.count_n}'] = self.pos.case.pop(pion)
                self.pos.position[self.pos_pion] = f'r{self.count_n}n'