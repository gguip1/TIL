import sys
input = sys.stdin.readline

B, N, M = map(int, input().split())
products = {}

for _ in range(N):
    name, price = input().split()
    products[name] = int(price)

for _ in range(M):
    B -= products[input().strip()]

if B >= 0:
    print("acceptable")
else:
    print("unacceptable")