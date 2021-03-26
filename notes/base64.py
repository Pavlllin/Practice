def inttob64(x,):
    n = int(x)
    # now convert decimal to 'to_base' base
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789+-*"
    res = ''
    ost =[]
    if x == 0:
        res +=alphabet[0]
        return res
    while n > 0:
        ost.append(n % 64)
        n = n // 64
    for i in ost:
        res +=alphabet[i]
    res = res[::-1]
    return res