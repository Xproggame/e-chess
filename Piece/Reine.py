from Piece.Deplacement import *

class Reine:

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
            3: [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]],
            4: [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
            5: [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]],
            6: [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0]],
            7: [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8]]
        }

    def mouvement(self, pion, couleur):
        self.list_move = []

        for x in range(7):
            coup = deplacement(self.pos, self.eat, self.position.get(x), pion, couleur)

            if coup != []:
                for element in coup:
                    self.list_move.append(element)

            for element in self.list_move:

                if element == -1:
                    self.list_move.remove(-1)