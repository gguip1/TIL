import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

# P = "I" + "OI" * N

P = "IOI"

result = 0

# for i in range(M - len(P) + 1):
#     if S[i:i + len(P)] == P:
#         result += 1

# search = False
# index = 0

# while index < M:
#     if S[index:index + len(P)] == P and not search:
#         result += 1
#         search = True
#         index += len(P)
#     elif search and S[index:index + 2] == "OI":
#         result += 1
#         index += 2
#     elif search:
#         search = False
#     else:
#         index += 1

count = 0
index = 0
while index < M:
    if S[index:index + len(P)] == P:
        count += 1
        index += 2
    elif count >= N:
        result += count - N + 1
        count = 0
        index += 1
    elif count < N:
        count = 0
        index += 1
    else:
        index += 1

print(result)
