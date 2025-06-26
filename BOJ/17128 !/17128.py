import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
cows = list(map(int, input().strip().split()))
cow_nums = list(map(int, input().strip().split()))

prefix_sum = [0] * N
for index in range(N):
    prefix_sum[index] = cows[index] * cows[(index + 1) % N] * cows[(index + 2) % N] * cows[(index + 3) % N]

total = sum(prefix_sum)

for cow_num in cow_nums:
    for _ in range(4):
        index = (cow_num - 1 - _) % N
        total -= prefix_sum[index]
    
    cows[cow_num - 1] *= -1
    
    for _ in range(4):
        index = (cow_num - 1 - _) % N
        prefix_sum[index] = (cows[index] * cows[(index + 1) % N] * cows[(index + 2) % N] * cows[(index + 3) % N])
        total += prefix_sum[index]
    
    print(total)