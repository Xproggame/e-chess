from Info.Mouvement import *
from Piece.Pion import *
from Piece.Reine import *
from Piece.Roi import *
from Piece.Tour import *
from Piece.cavalier import *
from Piece.fou import *
from Verification.In import *
from Verification.eat import *

info = Piece()
pos = Position()
conversion = Conversion(pos)
out = In()
eat = Eat(pos)
roi = Roi(pos, eat, out)
reine = Reine(pos, out, eat)
fou = Fou(pos, out, eat)
tour = Tour(pos, out, eat)
cavalier = Cavalier(pos, eat, out)
pion = Pion(pos, eat)

arbre = []
finish = False
couleur_player = ''
end = False
case = ''
fonction = {}
piece = ''
mouvement = {}
possible = False

while True:
    end = False

    while not finish:
        couleur_player = input("Quelle couleur voulez vous jouer ? [b, n] > ")

        if couleur_player == 'b':
            my_couleur = 'n'
            finish = True

        elif couleur_player == 'n':
            my_couleur = 'b'
            finish = True

        else:
            print("[ERROR] Couleur non valide")
            finish = False

    finish = False    

    while not end:

        if couleur_player == 'b':

            while not finish:
                case = input("Quelle piece voulez vous jouez ? [Coordonée] [lettre, chiffre] > ")
                case_un = conversion.convert.get(case[0]) + case[1]

                for cle in pos.position.keys():

                    if cle == case_un:

                        if pos.position.get(case_un) != '':
                            finish = True
                            piece = pos.position.get(case_un)
                            break

                        else:
                            print(f"[ERROR] Il n'y a pas de pièce à la position {case}.")
                            break

                    else:
                        print(f"[ERROR] La position {case} n'est pas valide.")
                        break

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
    
                for cle in pos.position.keys():
    
                    if cle == case_un:

                        for position in mouvement.get(piece):
                            possible = False

                            if position == case_un:
                                possible = True
                                finish = True
                                break

                        if not possible:
                            print(f"[ERROR] La position {case} n'est pas valide.")
                            break

                        else:
                            break
    
                    else:
                        print(f"[ERROR] La position {case} n'est pas valide.")
                        break
    
            finish = False