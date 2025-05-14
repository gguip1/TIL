import sys

MAX_VALUE = 10001

dp = [1] * MAX_VALUE

for val in range(2, MAX_VALUE):
    dp[val] += dp[val - 2]

for val in range(3, MAX_VALUE):
    dp[val] += dp[val - 3]

# A1. TLE
# for val in range(MIN_VALUE, MAX_VALUE):
#     answer = 0
    
#     queue = [(1, 1), (2, 2), (3, 3)]
    
#     while queue:
#         current_sum, prev_val = queue.pop(0)
        
#         if current_sum == val:
#             answer += 1

#         if prev_val == 1:
#             for add_val in [1]:
#                 if current_sum + add_val <= val:
#                     queue.append((current_sum + add_val, add_val))
#         elif prev_val == 2:
#             for add_val in [1, 2]:
#                 if current_sum + add_val <= val:
#                     queue.append((current_sum + add_val, add_val))
#         elif prev_val == 3:
#             for add_val in [1, 2, 3]:
#                 if current_sum + add_val <= val:
#                     queue.append((current_sum + add_val, add_val))
    
#     dp.append(answer)

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])