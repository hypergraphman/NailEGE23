def alg(n):
    s1 = f'{n:b}'.rjust(8, '0')
    s2 = ''
    for c in s1:
        if c == '0':
            s2 += '1'
        else:
            s2 += '0'
    s3 = int(s2, 2) + 1
    return s3


print(alg(80))