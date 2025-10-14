import sys
import copy

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

t = int(sys.stdin.readline().strip())

for i in range(t):
    Q = list(map(int, sys.stdin.readline().strip().split()))
    n = Q[0]
    arr = Q[1:1+n]
    
    prefixSum = []
    
    for x in range(n):
        if x == 0:
            prefixSum.append(arr[x])
        else:
            prefixSum.append(prefixSum[x - 1] + arr[x])

## 시간초과 pypy3로 맞은 경우
# for i in range(t):
#     Q = list(map(int, sys.stdin.readline().strip().split()))
#     n = Q[0]
#     arr = Q[1:1+n]
    
#     prefixSum = 0
#     result = None
    
#     for y in range(n):
#         for x in range(y, n):
#             if x == y:
#                 prefixSum = arr[x]
#             else:
#                 prefixSum += arr[x]
#                 if is_prime(prefixSum):
#                     if result is None:
#                         result = arr[y:x + 1]
#                         break
#                     else:
#                         if len(result) > len(arr[y:x + 1]):
#                             result = arr[y:x + 1]
#                             break
    
#     if result:
#         print(f'Shortest primed subsequence is length {len(result)}:', end=' ')
#         for r in result:
#             print(r, end=' ')
#         print()
#     else:
#         print('This sequence is anti-primed.')

## 시간초과 pypy로는 맞았는데..
# for i in range(t):
#     Q = list(map(int, sys.stdin.readline().strip().split()))
#     n = Q[0]
#     arr = Q[1:1+n]
    
#     find = False
#     result = None
    
#     if n < 2:
#         print('This sequence is anti-primed.')
#     else:
#         for x in range(2, n):
#             for y in range(n - x + 1):
#                 if is_prime(sum(arr[y:y+x])):
#                     find = True
#                     result = arr[y:y+x]
#                     break
#             if find:
#                 break
#         if result:
#             print(f'Shortest primed subsequence is length {len(result)}:', end=' ')
#             for r in result:
#                 print(r, end=' ')
#             print()
#         else:
#             print('This sequence is anti-primed.')
