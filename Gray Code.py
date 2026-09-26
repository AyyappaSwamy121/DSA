def grayToBinary(g):
    b = 0
    while g:
        b ^= g
        g >>= 1
    return b
