import sys

words = ["pi", "ka", "chu"]

S = sys.stdin.readline().strip()

index = 0
result = bool(S)

while index < len(S):
    if S[index:index + 2] in words:
        index += 2
        continue
    
    if S[index:index + 3] in words:
        index += 3
        continue
    
    result = False
    break

if result:
    print("YES")
else:
    print("NO")
