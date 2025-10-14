import sys
input = sys.stdin.readline

S = input().strip()
current = S[0]

a_b = 0
b_a = 0

if current == '0':
    a_b += 1
else:
    b_a += 1

for s in S:
    if s == '0' and s != current:
        current = s
        a_b += 1
    
    if s == '1' and s != current:
        current = s
        b_a += 1

print(min(a_b, b_a))
