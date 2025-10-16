import sys
input = sys.stdin.readline

N = int(input())

left = 0
right = 2 * N + (N - 2) * 2 + 1

middle = (N - 2) * 2 + 1

print('*' * N + ' ' * ((N - 2) * 2 + 1) + '*' * N)
for idx in range((N - 2) * 2 + 1):
    if idx < ((N - 2) * 2 + 1) // 2:
        left += 1
        right -= 1
        middle -= 2
        print(left * ' ' + '*' + (N - 2) * ' ' + '*' + (middle) * ' ' + '*' + (N - 2) * ' ' + '*')
    elif idx == ((N - 2) * 2 + 1) // 2:
        left += 1
        right -= 1
        print((N - 1) * ' ' + '*' + (N - 2) * ' ' + '*' + ' ' * (N - 2) + '*')
    else:
        left -= 1
        right += 1
        print(left * ' ' + '*' + (N - 2) * ' ' + '*' + (middle) * ' ' + '*' + (N - 2) * ' ' + '*')
        middle += 2
print('*' * N + ' ' * ((N - 2) * 2 + 1) + '*' * N)
