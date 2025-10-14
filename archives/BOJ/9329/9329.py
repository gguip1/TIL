import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    prizes = []
    for __ in range(n):
        prizes.append(list(map(int, input().split())))

    prizes.sort(key=lambda x: x[1] / x[x[0] - 2], reverse=True)
    stickers = list(map(int, input().split()))

    answer = 0

    for prize in prizes:
        check_v = float('inf')
        for v in range(prize[0]):
            check_v = min(check_v, stickers[prize[v + 1] - 1])

        for v in range(prize[0]):
            stickers[prize[v + 1] - 1] -= check_v

        answer += check_v * prize[-1]
    
    print(answer)