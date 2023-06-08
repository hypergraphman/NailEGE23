v, n, *a = map(int, open('26_225.txt').read().split())
a.sort(reverse=True)
last = 0
c = 0
for el in a:
    if v - el >= 0:
        c += 1
        last = el
        v -= el
print(c, last)