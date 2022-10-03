from itertools import permutations


def alg(n):
    a = set()
    for d1, d2 in permutations(str(n), r=2):
        num = int(d1 + d2)
        if 10 <= num <= 99:
            a.add(num)
    return max(a) - min(a)


print(alg(351))

i = 100
while alg(i) != 40:
    i += 1
print(i)
