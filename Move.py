from Info.Board import Board
from Piece.Reine import Reine
from Piece.cavalier import Cavalier
from Piece.Pion import Pion
from Piece.fou import Fou
from Piece.Tour import Tour
from Piece.Roi import Roi
from Verification.eat import Eat
from Info.Pièce import Piece


class Move:

    def __init__(self, board: Board, pion: Pion, cavalier: Cavalier, fou: Fou, tour: Tour, reine: Reine, roi: Roi, eat: Eat, list_piece: Piece):
        self.board = board
        self.pion = pion
        self.cavalier = cavalier
        self.fou = fou
        self.tour = tour
        self.reine = reine
        self.roi = roi
        self.eat = eat
        self.list_piece = list_piece
        self.list_fonction = {
            'p': self.pion.mouvement(piece, color),
            't': self.tour.mouvement(piece, color),
            'c': self.cavalier.mouvement(piece, color),
            'f': self.fou.mouvement(piece, color),
            'r': self.reine.mouvement(piece, color),
            'R': self.roi.mouvement(piece, color)
        }
        self.couleur = {
            'b': self.list_piece.piece_b,
            'n': self.list_piece.piece_n
        }
        self.list_move: {}

    def move(self, color):

        for piece in self.couleur.get(color):
            self.list_fonction.get(piece[0])()