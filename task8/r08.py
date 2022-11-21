from itertools import permutations

i = 0
for s in permutations('uley', r=4):
    word = ''.join(s)
    if word[0] != 'y' and 'eu' not in word:
        i += 1
print(i)