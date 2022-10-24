from itertools import permutations

for n in range(100, 999 + 1):
    a = [int(d1 + d2) for d1, d2 in permutations(str(n), r=2) if 10 <= int(d1 + d2) <= 99]
    if max(a) - min(a) == 60:
        print(n)