from itertools import product

i = 0
for s in product('egy', repeat=5):
    word = ''.join(s)
    if word[0] != 'g':
        i += 1
print(i)
