N = int(input())

answer_1 = 0
answer_2 = 0

for n in range(N):
    answer_1 += n + 1
    answer_2 += (n + 1) ** 3

print(answer_1)
print(answer_1 ** 2)
print(answer_2)