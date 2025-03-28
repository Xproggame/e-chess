class Sort:

    def __init__(self):
        self.plus_grande_valeur = -100000

    def tri(self, point):

        if point > self.plus_grande_valeur:
            self.plus_grande_valeur = point
            return True

        else:
            return False