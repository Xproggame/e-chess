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