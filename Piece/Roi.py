from Piece.Deplacement import *


class Roi:

    def __init__(self, pos: Position, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_possible = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
        self.list_pos_pion = []
        self.pos_pion = ''

    def mouvement(self, pion, couleur):
        self.list_move.append(deplacement(self.pos, self.eat, self.position.get(x), pion, couleur))

        for element in self.list_move:

            if element == -1:
                self.list_move.remove(-1)