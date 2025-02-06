from Info.Pos import Position
from Verification.eat import Eat
from Verification.In import In

class Reine:

    def __init__(self, pos: Position, out: In, eat: Eat):
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
        list_possible_cinq = [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]
        list_possible_six = [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8]]
        list_possible_sept = [[-1, 0], [-2, 0], [-3, 0], [-4, 0], [-5, 0], [-6, 0], [-7, 0], [-8, 0]]
        list_possible_huit = [[0, -1], [0, -2], [0, -3], [0, -4], [0, -5], [0, -6], [0, -7], [0, -8]]
        self.list_move = []
        self.pos_pion = str(self.pos.case.get(pion)[0]) + str(self.pos.case.get(pion)[1])
        self.list_pos_pion = [int(self.pos_pion[0]), int(self.pos_pion[1])]

        for element in list_possible_un:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_deux:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_trois:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_quatre:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_cinq:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_six:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_sept:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break

        for element in list_possible_huit:
            pos = str(self.pos.case.get(pion)[0] + element[0]) + str(self.pos.case.get(pion)[1] + element[1])
            self.eat.eat(pos, couleur)
            self.out.out(pos)

            if not self.out.out and not self.eat.bloque:

                if self.eat.possibilite:
                    self.list_move.append([pos, self.eat.point])

                else:
                    self.list_move.append([pos])

            else:
                break