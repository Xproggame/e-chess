class In:

    def __init__(self, ):
        self.out = False

    def out(self, pos):
        position = pos

        if 0 < position[0] < 9 and 0 < position[1] < 9:
            self.out = False

        else:
            self.out = True