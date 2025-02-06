from Info.Mouvement import *
from Piece.Pion import *
from Piece.Reine import *
from Piece.Roi import *
from Piece.Tour import *
from Piece.cavalier import *
from Piece.fou import *
from Verification.In import *
from Verification.eat import *

piece = Piece()
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

while True:

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
