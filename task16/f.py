from functools import lru_cache


@lru_cache(None)
def f(x):
    if x < 3:
        return 1
    if x >= 3:
        return f(x - 2) + f(x - 1)


x = int(input())
for i in range(1, x, 100):
    f(i)

print(f(x))

cur = 1
nxt = 1
for i in range(2, x + 1):
    t = cur
    cur = nxt
    nxt = t + nxt
print(cur)
#
# a = [0] * (x + 10)
# for i in range(1, x + 1):
#     if i < 3:
#         a[i] = 1
#     if i >= 3:
#         a[i] = a[i - 2] + a[i - 1]
#
# print(a[x])