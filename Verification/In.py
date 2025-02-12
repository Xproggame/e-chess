def out(pos: str):
    position = pos

    if 0 < int(position[0]) < 9 and 0 < int(position[1]) < 9:
        return False

    else:
        return True