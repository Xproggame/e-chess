from Info.Board import *


class Conversion:

    def __init__(self, board: Board):
        self.board = board
        self.convert = {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
            'e': '5',
            'f': '6',
            'g': '7',
            'h': '8'
        }
        self.deconvert = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h'
        }

    def move(self, x: int, y: int, piece):
        self.board.position[str(self.board.case.get(piece)[0]) + str(self.board.case.get(piece)[1])] = ''
        self.board.case[piece][0] = x
        self.board.case[piece][1] = y
        self.board.position[str(x) + str(y)] = piece
