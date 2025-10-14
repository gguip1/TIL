import sys
input = sys.stdin.readline

N = int(input())
qualities = sorted(list(map(int, input().split())))

if N == 1:
    print(qualities[0])
    sys.exit()

answer = 0

if N % 2 == 0:
    for idx in range(N // 2):
        answer += qualities[N - idx - 1] * 2
else:
    for idx in range(N // 2 - 1):
        answer += qualities[N - idx - 1] * 2
    
    if qualities[N // 2] * 3 > qualities[N // 2 + 1] * 2 + qualities[N // 2]:
        answer += qualities[N // 2] * 3
    else:
        answer += qualities[N // 2 + 1] * 2 + qualities[N // 2]
    
print(answer)