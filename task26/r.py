v, n, *a = map(int, open('26.txt').read().split())
# print(a, v, n)
a.sort()
k_people = 0
i = 0
while i < n and a[i] <= v:
    v -= a[i]
    i += 1
    k_people += 1
v += a[i - 1]
mx = a[i - 1]
while i < n and a[i] <= v:
    mx = a[i]
    i += 1
print(k_people, mx)