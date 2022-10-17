def alg(n):
    s1 = f'{n:b}'.rjust(8, '0')
    s2 = s1[:2] + s1[-2:]
    return int(s2, 2)


i = 131
while alg(i) != 10:
    i += 1
print(i)