from itertools import product

i = 0
for s in product('vesna', repeat=3):
    word = ''.join(s)
    if word.count('a') >= 1:
        i += 1
print(i)
