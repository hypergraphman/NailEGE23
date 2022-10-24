k = 0
a = set()
for n in range(1, 1000):
    s = bin(n)[2:]
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    r = int(s, 2)
    if 210 <= r <= 260:
        a.add(r)
print(len(a))