N = int(input())

scores = list(map(int, input().split()))
M = max(scores)

def new_score(score, M):
    return score / M * 100

amount = 0

for score in scores:
    amount += new_score(score, M)

print(amount / N)
