import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

if K >= N:
    print(0)
    sys.exit()

sensors = sorted(list(map(int, input().split())))
sensors_diff = []

for idx in range(N - 1):
    sensors_diff.append(sensors[idx + 1] - sensors[idx])

sensors_diff.sort()

for _ in range(K - 1):
    sensors_diff.pop()

print(sum(sensors_diff))
