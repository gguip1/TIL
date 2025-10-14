import sys

N, M = map(int, sys.stdin.readline().strip().split())

bucket = [_ + 1 for _ in range(N)]

for _ in range(M):
    X, Y = map(int, sys.stdin.readline().strip().split())
    reverse_bucket = bucket[X-1:Y]
    reverse_bucket.reverse()
    bucket[X-1:Y] = reverse_bucket

for _ in bucket:
    print(_, end=' ')
