class Piece:

    def __init__(self):
        self.piece_b = [
            'tb1',
            'cb1',
            'fb1',
            'rb',
            'Rb',
            'fb2',
            'cb2',
            'tb2',
            'pb1',
            'pb2',
            'pb3',
            'pb4',
            'pb5',
            'pb6',
            'pb7',
            'pb8',
        ]
        self.piece_n = [
            'tn1',
            'cn1',
            'fn1',
            'rn',
            'Rn',
            'fn2',
            'cn2',
            'tn2',
            'pn1',
            'pn2',
            'pn3',
            'pn4',
            'pn5',
            'pn6',
            'pn7',
            'pn8',
        ]
        self.point = {
            'p': 1,
            'c': 3,
            'f': 3,
            't': 4,
            'r': 12,
            'R': 41
        }
        self.ez_point = 0

    def find_point(self, piece):
        self.ez_point = self.point.get(piece[0])
