s = '100' + '7' + '0'*67
print(len(s))
while '900' in s or '8000' in s or '70' in s:
    s = s.replace('70', '8', 1)
    s = s.replace('900', '70', 1)
    s = s.replace('8000', '900', 1)
print(s)