from Piece.Deplacement import *


class Cavalier:

    def __init__(self, pos: Board, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_possible = [[2, -1], [2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2]]
        self.list_pos_pion = []
        self.pos_pion = ''

    def mouvement(self, pion, couleur):
        self.list_move.append(deplacement(self.pos, self.eat, self.list_possible, pion, couleur))

        for element in self.list_move:

            if element == -1:
                self.list_move.remove(-1)