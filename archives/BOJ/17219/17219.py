import sys

N, M = map(int, sys.stdin.readline().strip().split())

M_dict = {}

for _ in range(N):
    url, pwd = sys.stdin.readline().strip().split()
    M_dict[url] = pwd

for _ in range(M):
    url = sys.stdin.readline().strip()
    print(M_dict[url])
