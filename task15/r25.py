for a in range(1, 100):
    is_a = True
    for x in range(1, 100):
        s1 = x & 125 != 1
        s2 = x & 34 == 2
        s3 = x & a == 0
        if not (s1 or (s2 <= s3)):
            is_a = False
            break
    if is_a:
        print(a)
        break


for a in range(1, 1000):
    if all((x & 125 != 1) or ((x & 34 == 2) <= (x & a == 0)) for x in range(1, 1000)):
        print(a)
        break
