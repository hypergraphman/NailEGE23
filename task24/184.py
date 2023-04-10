s = open('24-181.txt').read().strip()
words = s.split('.')
lens, c = [],  []
for word in words:
    lens.append(len(word))
for i in range(len(words) - 4):
    c.append(len(words[i] + words[i + 1] + words[i + 2] + words[i + 3] + words[i + 4]))
print(max(c) + 4)