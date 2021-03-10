def inttob64(x,):
    n = int(x)
    # now convert decimal to 'to_base' base
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789+-"
    print(n)
    res = ''
    while n >0:
        res += alphabet[n]
        n = n //64
    return res