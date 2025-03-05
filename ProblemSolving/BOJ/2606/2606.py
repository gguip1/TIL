import sys

N = [[] for x in range(int(sys.stdin.readline().strip()))]
result = [0 for x in range(len(N))]

P = int(sys.stdin.readline().strip())

for i in range(P):
    A, B = map(int, sys.stdin.readline().strip().split())
    N[A - 1].append(B)
    N[B - 1].append(A)

def graphSearch(n = 1):
    result[n - 1] = 1
    for i in N[n - 1]:
        if result[i - 1] == 0:
            graphSearch(i)

graphSearch()
print(sum(result) - 1)
