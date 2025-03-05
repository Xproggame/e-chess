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
        self.noeud = 0
        self.super_noeud = 0
        self.list_piece = {
            'b': self.piece.piece_b,
            'n': self.piece.piece_n
        }
        self.actual_board = {}

    def create_arbre(self, color):
        self.actual_board = self.board.position
        self.move.move(color)

        for piece in self.list_piece.get(color):

            for move in self.move.list_move.get(piece):
                self.arbre[f'{str(self.super_noeud)}.{str(self.noeud)}'] = [piece, move[0], move[1], self.actual_board]