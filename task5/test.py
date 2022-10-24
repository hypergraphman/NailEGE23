k = 0
a = set()
for n in range(1, 1000):
    s = bin(n)[2:]
    r = 250
    if 210 <= r <= 260:
        a.add(r)
        k += 1
print(len(a))
print(k)