from itertools import permutations

alf = 'magistr'
s = set()
for let in permutations(alf, r=5):
    word = ''.join(let)
    if word.count('a') + word.count('i') <= 1:
        s.add(word)
print(len(s))