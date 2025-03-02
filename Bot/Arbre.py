from Bot.Move import Move
from Info.Pièce import Piece
from Info.Board import Board
from Info.Mouvement import Conversion


class Arbre:

    def __init__(self, move: Move, piece: Piece, board: Board, movement: Conversion):
        self.mouvement = movement
        self.board = board
        self.piece = piece
        self.move = move
        self.arbre = {}
        self.list_piece = {
            'b': self.piece.piece_b,
            'n': self.piece.piece_n
        }
        self.actual_board = {}

    def create_arbre(self, color):
        self.actual_board = self.board.position
        self.move.move(color)