def alg(n):
    s1 = f'{n:b}'
    s2a = s1 + str(sum(map(int, s1)) % 2)
    s2b = s2a + str(sum(map(int, s2a)) % 2)
    return int(s2b, 2)


print(alg(28))

i = 1
while alg(i) <= 77:
    i += 1
print(i)

for i in range(10**10):
    if alg(i) > 77:
        print(i)
        break