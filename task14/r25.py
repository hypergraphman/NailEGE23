def n_to_p(n, p):
    alf = '0123456789ABCDEF'
    r = ''
    while n > 0:
        r = alf[n % p] + r
        n //= p
    return r


print(n_to_p(49**7 + 7**21 - 7, 7).count('6'))