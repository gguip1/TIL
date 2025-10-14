import sys
input = sys.stdin.readline

N = int(input())

f_2 = [0] * N
f_matrix = [list(map(int, input().split())) for _ in range(N)]

for idx in range(N):
    
