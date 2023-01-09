f = 1
n = int(input())
for i in range(1, n + 1):
    f *= i
print(f)

def f(n):
    if n < 2:
        return 1
    if n >= 2:
        return n * f(n - 1)

print(f(n))
