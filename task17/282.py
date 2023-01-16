# a = [int(x) for x in open('17-282.txt').readlines()]
a = list(map(int, open('17-282.txt').readlines()))
mn17 = 10**10
for el in a:
    if el % 17 == 0 and el < mn17:
        mn17 = el
mx = -10**10
c = 0
for i in range(len(a) - 1):
    p1, p2 = a[i], a[i + 1]
    if p1 % mn17 == 0 or p2 % mn17 == 0:
        c += 1
        if p1 + p2 > mx:
            mx = p1 + p2
print(c, mx)
