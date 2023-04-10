
for i in range(174457, 174506):
    deliteli_i = set()
    for x in range(2, int(i ** 0.5) + 1):
        if i % x == 0:
            deliteli_i.add(x)
            deliteli_i.add(i // x)
            break
    deliteli_i = sorted(deliteli_i)
    if len(deliteli_i) == 2:
        print(deliteli_i[0], deliteli_i[1])
