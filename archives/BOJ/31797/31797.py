import sys
input = sys.stdin.readline

N, M = map(int, input().split())

hands = []

for _ in range(M):
    h1, h2 = map(int, input().split())
    hands.append((_ + 1, h1))
    hands.append((_ + 1, h2))

hands.sort(key=lambda x: x[1])

print(hands[N % (M * 2) - 1][0])
