import sys
input = sys.stdin.readline

N, M = map(int, input().split())
buckets = [v + 1 for v in range(N)]

for _ in range(M):
    i, j = map(int, input().split())
    buckets[i - 1], buckets[j - 1] = buckets[j - 1], buckets[i - 1]

print(*buckets)
