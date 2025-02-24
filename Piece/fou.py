from Info.Pos import Position
from Verification.eat import Eat
from Verification.In import *


class Fou:

    def __init__(self, pos: Position, eat: Eat):
        self.out = out
        self.pos = pos
        self.eat = eat
        self.list_move = []
        self.list_pos_pion = []
        self.pos_pion = ''

    def mouvement(self, pion, couleur):
        list_possible_un = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8]]
        list_possible_deux = [[-1, 1], [-2, 2], [-3, 3], [-4, 4], [-5, 5], [-6, 6], [-7, 7], [-8, 8]]
        list_possible_trois = [[-1, -1], [-2, -2], [-3, -3], [-4, -4], [-5, -5], [-6, -6], [-7, -7], [-8, -8]]
        list_possible_quatre = [[1, -1], [2, -2], [3, -3], [4, -4], [5, -5], [6, -6], [7, -7], [8, -8]]
        self.list_move = []
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        for element in list_possible_un:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)

            if not out(pos) and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])
                    break

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_deux:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)

            if not out(pos) and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])
                    break

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_trois:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)

            if not out(pos) and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])
                    break

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_quatre:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)

            if not out(pos) and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])
                    break

                else:
                    self.list_move.append([pos])

            else:
                break