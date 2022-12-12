from itertools import product

alf = 'pirog'
k = 0
for let in product(alf, repeat=5):
    word = ''.join(let)
    if (word.count('r') == 0
       or (word.count('r') == 1 and ('ri' in word or 'ro' in word))
       or (word.count('r') == 2 and word.count('ri') + word.count('ro') == 2)):
        k+=1
print(k)