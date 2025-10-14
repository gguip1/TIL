import sys
input = sys.stdin.readline
S = input().strip()
str_list = [0] * 26

for s in S:
    str_list[ord(s.upper()) % 65] += 1

cnt = 0
max_index = 0
max_value = max(str_list)

for idx in range(26):
    if str_list[idx] == max_value:
        max_index = idx
        cnt += 1

if cnt > 1:
    print('?')
else:
    print(chr(max_index + 65))
