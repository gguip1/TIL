import sys
import math

adrenaline = 0

N = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))
e = list(map(int, sys.stdin.readline().strip().split()))
k = list(map(float, sys.stdin.readline().strip().split()))

# for i in range(N):
#     adrenaline += max(math.floor(a[i] * int(k[i] * 10)) // 10 - e[i], a[i] - math.floor(k[i] * int(e[i] * 10)) // 10)

for i in range(N):
    A = a[i]
    E = e[i]
    K = k[i] * 10
    if K >= 10:
        adrenaline += (math.floor(A * K) // 10 - E)
    else:
        adrenaline += (A - math.floor(E * K) // 10)

print(adrenaline)

# 3             
# 25 35 33
# 8 10 12
# 1.05 1.15 1.25
# 72