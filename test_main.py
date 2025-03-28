import unittest
from Info.Mouvement import *
from Piece.Pion import *
from Piece.Reine import *
from Piece.Roi import *
from Piece.Tour import *
from Piece.cavalier import *
from Piece.fou import *
from Verification.eat import *
from Bot.Move import Move
from Bot.Arbre import Arbre


class MyTestCase(unittest.TestCase):
    def test_something(self):
        info = Piece()
        board = Board()
        conversion = Conversion(board)
        eat = Eat(board, info)
        roi = Roi(board, eat)
        reine = Reine(board, eat)
        fou = Fou(board, eat)
        tour = Tour(board, eat)
        cavalier = Cavalier(board, eat)
        pion = Pion(board, eat)
        move = Move(board, pion, cavalier, fou, tour, reine, roi, eat, info)
        arbre = Arbre(move, info, board, conversion)

        couleur_player = ''
        piece = ''
        possible = False
        finish_color = False
        list_coup = [['e2', 'e4'], ['d1', 'd5']]

        while True:

            while not finish_color:
                couleur_player = 'b'

                if couleur_player == 'b':
                    my_couleur = 'n'
                    finish_color = True

                elif couleur_player == 'n':
                    my_couleur = 'b'
                    finish_color = True

                else:
                    print("[ERROR] Couleur non valide")
                    finish_color = False

            finish = False

            for coup in list_coup:

                if couleur_player == 'b':

                    while not finish:
                        case = coup[0]
                        case_un = conversion.convert.get(case[0]) + case[1]

                        for cle in board.position.keys():

                            if cle == case_un:

                                if board.position.get(case_un) != '':
                                    finish = True
                                    piece = board.position.get(case_un)
                                    break

                                else:
                                    print(f"[ERROR] Il n'y a pas de pièce à la position {case}.")
                                    break

                        if not finish:
                            print(f"[ERROR] La position {case} n'est pas valide.")

                    finish = False
                    fonction = {
                        'p': pion,
                        'c': cavalier,
                        'f': fou,
                        't': tour,
                        'r': reine,
                        'R': roi
                    }
                    fonction.get(piece[0]).mouvement(piece, 'b')
                    mouvement = {
                        'p': pion.list_move,
                        'c': cavalier.list_move,
                        'f': fou.list_move,
                        't': tour.list_move,
                        'r': reine.list_move,
                        'R': roi.list_move
                    }

                    while not finish:
                        case = coup[1]
                        case_un = conversion.convert.get(case[0]) + case[1]

                        for cle in board.position.keys():

                            if cle == case_un:
                                list_move = mouvement.get(piece[0])

                                for position in list_move:
                                    possible = False

                                    if position[0] == case_un:
                                        possible = True
                                        finish = True
                                        break

                                if not possible:
                                    print(f"[ERROR] La position {case} n'est pas valide.")
                                    break

                                else:
                                    break

                        if not finish:
                            print(f"[ERROR] La position {case} n'est pas valide.")

                    finish = False
                conversion.move(int(case_un[0]), int(case_un[1]), piece)

                if my_couleur == 'n':
                    coup_final = arbre.create_arbre(my_couleur, couleur_player)
                    case_piece = str(board.case.get(coup_final[1])[0]) + str(board.case.get(coup_final[1])[1])
                    conversion.move(int(coup_final[0][1]), int(coup_final[0][0]), coup_final[1])
                    print(f"Le Bot a joué la pièce {conversion.deconvert.get(case_piece[0]) + case_piece[1]} en {conversion.deconvert.get(coup_final[0][0]) + coup_final[0][1]}")

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
