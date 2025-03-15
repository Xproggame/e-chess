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

    def __init__(self, board: Board, pion: Pion, cavalier: Cavalier, fou: Fou, tour: Tour, reine: Reine, roi: Roi,
                 eat: Eat, list_piece: Piece):
        self.board = board
        self.pion = pion
        self.cavalier = cavalier
        self.fou = fou
        self.tour = tour
        self.reine = reine
        self.roi = roi
        self.eat = eat
        self.list_piece = list_piece
        self.couleur = {
            'b': self.list_piece.piece_b,
            'n': self.list_piece.piece_n
        }
        self.list_move = {}

    def move(self, color: str):
        self.list_move = {}

        for piece in self.couleur.get(color):
            list_fonction = {
                'p': self.pion,
                't': self.tour,
                'c': self.cavalier,
                'f': self.fou,
                'r': self.reine,
                'R': self.roi
            }
            list_fonction.get(piece[0]).mouvement(piece, color)
            list_move_search = {
                'p': self.pion.list_move,
                't': self.tour.list_move,
                'c': self.cavalier.list_move,
                'f': self.fou.list_move,
                'r': self.reine.list_move,
                'R': self.roi.list_move
            }

            if list_move_search.get(piece[0]) != []:
                self.list_move[piece[0]] = list_move_search.get(piece[0])