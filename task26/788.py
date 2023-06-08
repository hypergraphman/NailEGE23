vb, vm, n, *a = map(int, open('26_225.txt').read().split())
D, E = [], []
a.sort()
for i in a:
    if i > 500:
        D.append(i)
    else:
        E.append(i)
c1, c2, mx1, mx2 = 0, 0, 0, 0
E.sort()
for el in E:
    if vm - el >= 0:
        c1 += 1
        if el > mx1:
            mx1 = el
        vm -= el
D.sort()
for el in D:
    if vb - el >= 0:
        c2 += 1
        if el > mx2:
            mx2 = el
        vb -= el
print(c1 + c2, mx1 + mx2)