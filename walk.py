def is_valid_walk(walk):
    walk = list(walk)
    if len(walk) != 10 or len(walk) == 0:
        return False
    if walk[0] != walk[-1]:
        return False
    else:
        return True
    pass