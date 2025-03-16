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

    def create_arbre(self, my_color, color):
        self.arbre = {}
        arbre_iterrable = {}
        self.noeud = 0
        self.super_noeud = 0
        self.actual_board = self.board.position
        self.move.move(my_color)

        for piece in self.list_piece.get(my_color):

            if self.move.list_move.get(piece[0]) != None:

                for move in self.move.list_move.get(piece[0]):
                    self.arbre[f'{str(self.super_noeud)}.{str(self.noeud)}'] = [piece, move[0], move[1], self.actual_board, self.noeud]
                    self.noeud += 1

        self.super_noeud += 1
        self.noeud = 0
        arbre_iterrable = self.arbre.copy()

        for coup in arbre_iterrable.values():
            self.actual_board = self.board.position
            self.actual_board[coup[1]] = coup[0]
            case = self.board.case.get(coup[0])
            self.actual_board[str(case[0]) + str(case[1])] = ''
            self.move.move(color)

            for piece in self.list_piece.get(my_color):

                if self.move.list_move.get(piece[0]) != None:

                    for move in self.move.list_move.get(piece[0]):
                        self.arbre[f'{str(self.super_noeud)}.{str(self.noeud)}'] = [piece[0], move[0], move[1], self.actual_board]
                        self.noeud += 1
                        self.arbre[f'0.{coup[4]}'] = [coup[0], coup[1], coup[2] - move[1], coup[3], coup[4]]

        key_valide = []

        for key in self.arbre.keys():

            if key[0] == '0':
                key_valide.append(key)

        best = ['', 0]

        for key in key_valide:

            if self.arbre.get(key)[2] >= best[1] or best == ['', 0]:
                best = [key, self.arbre.get(key)[2]]

        return [self.arbre.get(best[0])[1], self.arbre.get(best[0])[0]]