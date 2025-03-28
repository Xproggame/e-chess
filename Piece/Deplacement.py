from Verification.eat import *

def deplacement(pos: Board, eat: Eat, list_possible, pion, couleur):
    list_move = []
    
    for element in list_possible:
        position = str(pos.case.get(pion)[0] + element[0]) + str(pos.case.get(pion)[1] + element[1])
        eat.eat(position, couleur)

        if not out(position) and not eat.bloque:

            if eat.possibilite:
                list_move.append([position, eat.point])


            else:
                list_move.append([position, 0])

        else:
            break

    return list_move