import sys

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

result = 'NO'
check = 1
for i in range(N - 1):
    if ord(S[i]) + 1 == ord(S[i + 1]) or ord(S[i]) - 1 == ord(S[i + 1]):
        check += 1
    else:
        check = 1
    
    if check == 5:
        result = 'YES'
        break

print(result)
