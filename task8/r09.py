from itertools import permutations
i = 0
for s in permutations('вуаль'):
    word = ''.join(s)
    if word[0] != 'ь' and 'ьу' not in word and 'ьа' not in word:
        i += 1
print(i)