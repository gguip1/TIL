import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arrival_times = [int(input()) for _ in range(N)]
diff_arrival_times = []

for i in range(N - 1):
    diff_arrival_times.append(arrival_times[i + 1] - arrival_times[i])

diff_arrival_times.sort(reverse=True)
answer = 1

for i in range(N - 1):
    if K > 1:
        answer += 1
        K -= 1
    else:
        answer += diff_arrival_times[i]

print(answer)