def find_it(seq):
    count = {}
    for n in seq:
        count[n] = count.get(n, 0)+1
        
    for n in count :
        if count[n] % 2 != 0:
            return n
