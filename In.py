from Mouvement import *

class In:

    def __init__(self, convert: Conversion):
        self.out = False

    def out(self, pos):
        position = pos
        position = convert.convert.get(position[0]) + position[2]

        if 0 < int(position[0]) < 9 and 0 < int(position[2]) < 9:
            self.out = False

        else:
            self.out = True