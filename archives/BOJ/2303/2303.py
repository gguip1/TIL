import sys

N = int(sys.stdin.readline().rstrip())
ps = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
ps_answers = []

for p in ps:
    max_value = 0
    
    for x in range(5 - 2):
        for y in range(x + 1, 5 - 1):
            for z in range(y + 1, 5):
                max_value = max((p[x] + p[y] + p[z]) % 10, max_value)
    
    ps_answers.append(max_value)

max_value = 0
answer = 0

for index, ps_answer in enumerate(ps_answers):
    if ps_answer >= max_value:
        max_value = ps_answer
        answer = index + 1

print(answer)
