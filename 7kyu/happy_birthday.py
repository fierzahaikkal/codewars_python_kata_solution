def wrap(height, width, length):
    dim = sorted([height, width, length])
    return 20 + dim[0]*4 + (dim[1]+dim[2]) * 2
