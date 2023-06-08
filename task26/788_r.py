v_d, v_e, n, *a = map(int, open('26_788.txt').read().split())
d = []
e = []
for el in a:
    if el > 500:
        d.append(el)
    else:
        e.append(el)
d.sort()
c1 = 0
last = 0
for el in d:
    if v_d - el >= 0:
        c1 += 1
        v_d -= el
        last = el
v_d += last
mx1 = 0
for el in d:
    if el > mx1 and el <= v_d:
        mx1 = el


e.sort()
c2 = 0
last = 0
for el in e:
    if v_e - el >= 0:
        c2 += 1
        v_e -= el
        last = el
v_e += last
mx2 = 0
for el in e:
    if el > mx2 and el <= v_e:
        mx2 = el
print(c1 + c2, mx1 + mx2)