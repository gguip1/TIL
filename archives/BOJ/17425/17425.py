import sys

input = sys.stdin.readline

MAX = 1000000

F_list = [0] * (MAX + 1)
G_list = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        F_list[j] += i

    G_list[i] = G_list[i - 1] + F_list[i]

T = int(input())
Q = [int(input().strip()) for x in range(T)]

for x in Q:
    print(G_list[x])
