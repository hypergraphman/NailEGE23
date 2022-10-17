for n in range(1000, 10000):
    d1, d2, d3, d4 = map(int, str(n))
    s1 = d1 + d2
    s2 = d2 + d3
    s3 = d3 + d4
    mx = max(s1, s2, s3)
    md = s1 + s2 + s3 - mx - min(s1, s2, s3)
    if str(md) + str(mx) == '210':
        print(n)
        break








