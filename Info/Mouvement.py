from Info.Board import *


class Conversion:

    def __init__(self, pos: Board):
        self.pos = pos
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
        pos_base = str(self.pos.case.get(piece))
        self.pos.position[pos_base[0] + pos_base[1]] = ''
        self.pos.case[piece][0] += y
        self.pos.case[piece][1] += x
        pos = str(self.pos.case.get[piece])
        self.pos.position[pos[0] + pos[1]] = piece
