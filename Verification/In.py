class In:

    def __init__(self):
        self.out = False

    def out(self, pos: str):
        position = pos

        if 0 < int(position[0]) < 9 and 0 < int(position[2]) < 9:
            self.out = False

        else:
            self.out = True