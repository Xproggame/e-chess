from Piece.Deplacement import *


class Cavalier:

    def __init__(self, pos: Board, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_possible = {
            0: [[2, -1]],
            1: [[2, 1]],
            2: [[1, 2]],
            3: [[-1, 2]],
            4: [[-2, 1]],
            5: [[-2, -1]],
            6: [[-1, -2]],
            7: [[1, -2]]
        }
        self.list_pos_pion = []
        self.pos_pion = ''

    def mouvement(self, pion, couleur):

        for x in range(7):
            coup = deplacement(self.pos, self.eat, self.list_possible.get(x), pion, couleur)

            if coup != -1:
                for element in coup:
                    self.list_move.append(element)

            for element in self.list_move:

                if element == -1:
                    self.list_move.remove(-1)