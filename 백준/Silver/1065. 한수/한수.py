import sys
input = sys.stdin.readline

N = int(input())
answer = 0

for n in range(1, N + 1):
    if n < 100:
        answer += 1
    else:
        str_n = str(n)
        if int(str_n[0]) - int(str_n[1]) == int(str_n[1]) - int(str_n[2]):
            answer += 1

print(answer)
