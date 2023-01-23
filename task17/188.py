a = list(map(int, open('17-7.txt').readlines()))
c = 0
s = 0
for i in range(2, len(a)):
    p1, p2, p3 = a[i - 2], a[i - 1], a[i]
    if p1 % 16 == 0 and p2 % 16 == 0 or p2 % 16 == 0 and p3 % 16 == 0 or p1 % 16 == 0 and p3 % 16 == 0:
        c += 1
        s += max([p1, p2, p3])
print(c, s)