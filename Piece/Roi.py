from Piece.Deplacement import *


class Roi:

    def __init__(self, pos: Board, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_possible = {
            0: [[1, 0]],
            1: [[1, 1]],
            2: [[0, 1]],
            3: [[-1, 1]],
            4: [[-1, 0]],
            5: [[-1, -1]],
            6: [[0, -1]],
            7: [[1, -1]]
        }
        self.list_pos_pion = []
        self.pos_pion = ''

    def mouvement(self, pion, couleur):
        for x in range(7):
            coup = deplacement(self.pos, self.eat, self.list_possible.get(x), pion, couleur)

            if coup != []:
                for element in coup:
                    self.list_move.append(element)

            for element in self.list_move:

                if element == -1:
                    self.list_move.remove(-1)