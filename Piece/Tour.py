from Piece.Deplacement import *


class Tour:

    def __init__(self, pos: Position, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_pos_pion = []
        self.pos_pion = ''
        self.position = {
            0: [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
            1: [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]],
            2: [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0]],
            3: [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8]]
        }

    def mouvement(self, pion, couleur):

        for x in range(3):

            deplacement(self.pos, self.eat, self.position.get(x), pion, couleur)
