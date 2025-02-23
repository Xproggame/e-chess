from Info.Pos import *
from Verification.In import *
from Verification.eat import *


def deplacement(pos: Pos, eat: Eat, list_possible):
    
    for element in list_possible:
        pos = str(pos.case.get(pion)[0] + element[0]) + str(pos.case.get(pion)[1] + element[1])
        eat.eat(pos, couleur)

        if not out(pos) and not eat.bloque:

            if eat.possibilite:
                return [pos, eat.point]
                break

            else:
                return [pos]

        else:
            break
