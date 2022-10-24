for n in range(100, 999 + 1):
    d1, d2, d3 = n // 100, n // 10 % 10, n % 10
    a = [d1 * 10 + d2, d2 * 10 + d1,
         d1 * 10 + d3, d3 * 10 + d1,
         d3 * 10 + d2, d2 * 10 + d3]
    mx = 0
    mn = 1000
    for el in a:
        if 10 <= el <= 99:
            if mx < el:
                mx = el
            if mn > el:
                mn = el
    if mx - mn == 60:
        print(n)