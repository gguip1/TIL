import sys
input = sys.stdin.readline

N = int(input())
T = 8
daldidalgo = 1

while True:
    if daldidalgo > N:
        print(T + 1)
        break
    elif daldidalgo == N:
        print(T + 2)
        break
    else:
        daldidalgo *= 2
        T += 1
