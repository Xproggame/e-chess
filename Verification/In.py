def out(pos: str):
    position = pos

    try:
        test = int(position)

    except:
        pass

    if 0 < int(position[0]) < 9 and 0 < int(position[1:]) < 9:
        return False

    else:
        return True