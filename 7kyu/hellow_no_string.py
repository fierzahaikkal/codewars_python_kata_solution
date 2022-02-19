def hello_world():
    lst = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    return str().join([chr(a) for a in lst])
    # Remember, no strings!
