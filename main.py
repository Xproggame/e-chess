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
                case = input("Quelle piece voulez vous jouez ? [Coordonée] [chiffre, lettre] > ")
                case_un = case[0] + conversion.convert.get(case[1])

                for cle in conversion.convert.keys():

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