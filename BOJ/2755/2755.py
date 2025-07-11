import sys
input = sys.stdin.readline

scores = {
    "A+": 4.3,
    "A0": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B0": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C0": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D0": 1.0,
    "D-": 0.7,
    "F": 0.0
}

credits = 0
score_ = 0

N = int(input())

for _ in range(N):
    _, credit, score = input().strip().split()
    credits += int(credit)
    score_ += (scores.get(score) * int(credit))

def func(value: int):
    if value % 10 >= 5:
        return value + 10 - (value % 10)
    else:
        return value - value % 10

print(f'{func(round(score_ / credits * 1000)) / 1000:.2f}')