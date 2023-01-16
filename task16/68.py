from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3:
        return n + 1
    if n >= 3 and n % 2 == 0:
        return f(n - 2) + n - 2
    return -1


for i in range(100, 10000, 100):
    f(i)

c = 0
for i in range(10000):
    if 10000 <= f(i) < 100000:
        c += 1
print(c)
