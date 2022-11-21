from itertools import permutations

a = set()
for s in permutations('капкан', r=6):
    word = ''.join(s)
    if 'аа' not in word and 'кк' not in word:
        a.add(word)
print(len(a))