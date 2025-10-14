import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
T, S = map(int, sys.stdin.readline().rstrip().split())

workHour = 8

Zip = 0
Dok = 0

if N % workHour == 0:
    Zip = N + S * (N // workHour - 1)
else:
    Zip = N + S * (N // workHour)

if M % workHour == 0:
    Dok = M + (T + T + S) * (M // workHour - 1) + T
else:
    Dok = M + (T + T + S) * (M // workHour) + T

if Zip > Dok:
    print('Dok')
    print(Dok)
else:
    print('Zip')
    print(Zip)

## 시간 초과
# while N > 0:
#     if N - workHour > 0:
#         Zip += workHour
#         N -= workHour
#         Zip += S
#     else:
#         Zip += N
#         N = 0

# while M > 0:
#     if M - workHour > 0:
#         Dok += T
#         Dok += workHour
#         M -= workHour
#         Dok += T
#         Dok += S
#     else:
#         Dok += T
#         Dok += M
#         M = 0

# if Zip < Dok:
#     print('Zip')
#     print(Zip)
# else:
#     print('Dok')
#     print(Dok)