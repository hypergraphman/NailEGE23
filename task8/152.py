from itertools import product

alf = 'abcd'
k = 0
for let in product(alf, repeat=5):
    if let[0] != 'a' and let[0] != let[2] and let[1] != let[3] and let[2] != let[4]:
        k+=1
print(k)