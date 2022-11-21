from itertools import product

for i, s in enumerate(product('klrt', repeat=4), start=1):
    word = ''.join(s)
    if i == 67:
        print(word)
