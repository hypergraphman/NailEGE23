s = open('24-181.txt').read().strip()
words = s.split('.')
lens, c = [],  []
for word in words:
    lens.append(len(word))
# print(words)
# print(lens)
for i in range(len(words) - 2):
    c.append(len(words[i] + words[i + 1] + words[i + 2]))
# print(c)
print(max(c) + 2)

