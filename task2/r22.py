print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = int((x or y) and (y != z) and not w)
                if f:
                    print(x, y, z, w)
print()

from itertools import product

print('x y z w')
for x, y, z, w in product((0, 1), repeat=4):
    f = int((x or y) and (y != z) and not w)
    if f:
        print(x, y, z, w)
