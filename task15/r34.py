for a in range(1, 100):
    is_a = True
    for k in range(1, 100):
        for n in range(1, 100):
            s1 = 5*k + 6*n > 57
            s2 = k <= a
            s3 = n < a
            if not (s1 or (s2 and s3)):
                is_a = False
                break
    if is_a:
        print(a)
        break