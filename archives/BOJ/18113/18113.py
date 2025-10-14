import sys

def kimbap(L, K):
    if L < K:
        return -1
    
    if L < 2 * K:
        L -= K
    else:
        L -= 2 * K
    
    return L
    

N, K, M = map(int, sys.stdin.readline().rstrip().split())

ks = []

for i in range(N):
    L = int(sys.stdin.readline().rstrip())
    
    k = kimbap(L, K)
    if k != -1:
        ks.append(k)

if len(ks) > 0:
    left = 1
    right = max(ks)

    P = -1

    while left <= right:
        mid = (right + left) // 2
        count = sum(k // mid for k in ks)

        if count >= M:
            P = mid
            left = mid + 1
        elif count < M:
            right = mid - 1
            
    print(P)
else:
    print(-1)