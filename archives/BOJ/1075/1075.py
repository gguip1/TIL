N = int(input())
F = int(input())

N = N - (N % 100)

for v in range(1, 100):
    if N % F == 0:
        break
    N += 1

print(str(N)[-2:])