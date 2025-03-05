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

finish = False
couleur_player = ''
end = False
case = ''
fonction = {}
piece = ''
mouvement = {}
possible = False
finish_color = False
list_move = []

while True:
    end = False

    while not finish_color:
        couleur_player = input("Quelle couleur voulez vous jouer ? [b, n] > ")

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

    while not end:

        if couleur_player == 'b':

            while not finish:
                case = input("Quelle piece voulez vous jouez ? [Coordonée] [lettre, chiffre] > ")
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
                'p': pion.mouvement(piece, 'b'),
                'c': cavalier.mouvement(piece, 'b'),
                'f': fou.mouvement(piece, 'b'),
                't': tour.mouvement(piece, 'b'),
                'r': reine.mouvement(piece, 'b'),
                'R': roi.mouvement(piece, 'b')
            }
            fonction.get(piece[0])
            mouvement = {
                'p': pion.list_move,
                'c': cavalier.list_move,
                'f': fou.list_move,
                't': tour.list_move,
                'r': reine.list_move,
                'R': roi.list_move
            }

            while not finish:
                case = input("Où voulez vous jouez cette pièce ? [Coordonée] [lettre, chiffre] > ")
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