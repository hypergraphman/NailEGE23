a = []
for x in range(100):
    for y in range(100):
        for z in range(100):
            if z + y == 26 and 2 * x + 3 * y + 6 * z == 186:
                print(x + y + z + 2)
                a.append(x + y + z + 2)
print(min(a))