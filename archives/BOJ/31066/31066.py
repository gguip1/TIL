import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N, M, K = map(int, input().split())
    a, b, c, d = N, M, 0, 0

    if K == 1 and M == 1 and M < N:
        print(-1)
    else:
        count = 0
        while True:
            a -= M * K
            count += 1
            if a <= 0:
                break
            a += 1
            count += 1
        print(count)
