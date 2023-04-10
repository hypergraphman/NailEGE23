k = 0
for i in range(3532000, 3532161):
    i_prostoe = True
    for x in range(2, int(i**0.5) + 1):
        if i % x == 0:
            i_prostoe = False
            break
    if i_prostoe:
        k += 1
        print(k, i)