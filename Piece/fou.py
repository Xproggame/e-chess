from Piece.Deplacement import *


class Fou:

    def __init__(self, pos: Board, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_pos_pion = []
        self.pos_pion = ''
        self.position = {
            0: [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]],
            1: [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8]],
            2: [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8]],
            3: [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]]
        }

    def mouvement(self, pion, couleur):

        for x in range(3):
            coup = deplacement(self.pos, self.eat, self.position.get(x), pion, couleur)

            if coup != []:
                for element in coup:
                    self.list_move.append(element)

            for element in self.list_move:

                if element == -1:
                    self.list_move.remove(-1)
