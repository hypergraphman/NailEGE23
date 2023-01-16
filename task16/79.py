from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 5:
        return n
    else:
        if n % 3 == 0:
            return n + f(n//3 + 1)
        else:
            return None

for i in range(100, 10000, 100):
    try:
        f(i)
    except:
        pass
fm = 0
for i in range(10000):
    try:
        if f(i) > 1000:
            fm = i
            break
    except:
        pass
print(fm)