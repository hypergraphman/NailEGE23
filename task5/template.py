def alg(n):
    pass


i = 1
while alg(i) <= 100500:
    i += 1
print(i)

for i in range(10**10):
    if alg(i) > 100500:
        print(i)
        break