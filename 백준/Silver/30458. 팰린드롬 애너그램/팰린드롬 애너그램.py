import sys
input = sys.stdin.readline

N = int(input())
S = input().rstrip()

alpha = [0] * 26

for s in S:
    alpha[ord(s) - ord('a')] += 1

if (N % 2 == 1):
    alpha[ord(S[N // 2]) - ord('a')] -= 1

for a in alpha:
    if a % 2 == 1:
        print("No")
        sys.exit()

print("Yes")
