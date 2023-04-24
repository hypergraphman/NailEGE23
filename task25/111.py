def divs(n):
    res = {1, n}
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


k = 0
s = 0
for i in range(264871, 322989 + 1):
    t = divs(i)
    if len(t) == 4 and t[1] % 10 == t[2] % 10:
        s += i
        k += 1
        print(t)

print(k, s // k)