print('x y w z')
for x in 0,1:
    for y in 0, 1:
        for w in 0, 1:
            for z in 0, 1:
                if int((x and not y) or ((not w) or z)) == (z == x):
                    print(x, y, w, z)
