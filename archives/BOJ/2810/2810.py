import sys
input = sys.stdin.readline

N = int(input())
seats = input()

answer = 1

couple_seat_cnt = 0

for idx in range(len(seats)):
    if seats[idx] == 'S':
        answer += 1
    else:
        if couple_seat_cnt == 0:
            couple_seat_cnt += 1
        else:
            answer += 1
            couple_seat_cnt = 0

print(min(answer, N))
