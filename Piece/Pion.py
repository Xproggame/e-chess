from Verification.eat import *


class Pion:

    def __init__(self, pos: Board, eat: Eat):
        self.eat = eat
        self.board = pos
        self.pos_pion = ''
        self.list_pos_pion = []
        self.list_move = []
        self.count_b = 0
        self.count_n = 0
        self.avant = 0

    def mouvement(self, pion: str, couleur):
        self.list_move = []
        self.pos_pion = str(self.board.case.get(pion)[0]) + str(self.board.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        if couleur == 'b':
            self.avant = 1

        else:
            self.avant = -1

        position = str(self.board.case.get(pion)[0]) + str(self.board.case.get(pion)[1] + self.avant)
        self.eat.eat(position, couleur)

        if not self.eat.bloque:

            if not self.eat.pion_adverse:
                self.list_move.append([position, 0])

        position = str(self.board.case.get(pion)[0]) + str(self.board.case.get(pion)[1] + self.avant * 2)
        self.eat.eat(position, couleur)

        if not self.eat.bloque and self.board.case.get(pion)[1] == 2:

            if not self.eat.pion_adverse:
                self.list_move.append([position, 0])

        position = str(self.board.case.get(pion)[0] + 1) + str(self.board.case.get(pion)[1] + self.avant)
        self.eat.eat(position, couleur)

        if self.eat.possibilite:

            if not out(position):
                self.list_move.append([position, self.eat.point])

        position = str(self.board.case.get(pion)[0] - 1) + str(self.board.case.get(pion)[1] + self.avant)
        self.eat.eat(position, couleur)

        if self.eat.possibilite:

            if not out(position):
                self.list_move.append([position, self.eat.point])

    def promotion(self, pion):

        if self.board.case.get(pion)[0] + self.avant == 8 or self.board.case.get(pion)[0] + self.avant == 1:

            if self.avant == 1:
                self.count_b += 1
                self.board.case[f'r{self.count_b}'] = self.board.case.pop(pion)
                self.board.position[self.pos_pion] = f'r{self.count_b}b'
            
            else:
                self.count_n += 1
                self.board.case[f'r{self.count_n}'] = self.board.case.pop(pion)
                self.board.position[self.pos_pion] = f'r{self.count_n}n'