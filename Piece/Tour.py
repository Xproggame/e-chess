from Info.Pos import Position
from Verification.eat import Eat
from Verification.In import In
from Piece.Deplacement import *


class Tour:

    def __init__(self, pos: Position, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_pos_pion = []
        self.pos_pion = ''

    def mouvement(self, pion, couleur):
        list_possible_un = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]
        list_possible_deux = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]
        list_possible_trois = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0]]
        list_possible_quatre = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8]]
        self.list_move = []
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        for x in range(3):

            deplacement(self.pos, self.eat, )
