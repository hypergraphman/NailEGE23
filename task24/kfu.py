s = open('24kfu.txt').read().strip()
cur_len = 1
mx_len = 1
i_end_mx_line = 0
for i in range(1, len(s)):
    if s[i - 1] <= s[i]:
        cur_len += 1
        if cur_len > mx_len:
            mx_len = cur_len
            i_end_mx_line = i
    else:
        cur_len = 1
print(mx_len)
print(s[i_end_mx_line - mx_len + 1: i_end_mx_line + 1])