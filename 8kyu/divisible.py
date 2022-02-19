def is_divisible(n,x,y):
    x = n % x
    y = n % y
    if x == 0 and y == 0:
        return True
    else:
        return False
