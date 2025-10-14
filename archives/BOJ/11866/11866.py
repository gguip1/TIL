import sys
input = sys.stdin.readline

N, K = map(int, input().split())

_list = [i for i in range(1, N + 1)]
answer = list()
now = 0
while _list:
    now = (now + K - 1) % len(_list)
    answer.append(_list.pop(now))

print('<', end='')
print(*answer, sep=', ', end='')
print('>')