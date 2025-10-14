import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

u_list = [1] * N
d_list = [1] * N

for i in range(1, N):
    if seq[i - 1] <= seq[i]:
        u_list[i] = u_list[i - 1] + 1
    if seq[i - 1] >= seq[i]:
        d_list[i] = d_list[i - 1] + 1

print(max(max(u_list), max(d_list)))