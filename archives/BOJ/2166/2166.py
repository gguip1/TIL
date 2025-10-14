import sys
input = sys.stdin.readline

N = int(input())
coordinates = [list(map(int, input().split())) for _ in range(N)]

answer = 0

# 신발끈 공식
prev_x = None
prev_y = None

for x, y in coordinates:
    if prev_x is not None and prev_y is not None:
        answer += prev_x * y
        answer -= prev_y * x
    prev_x = x
    prev_y = y

answer += coordinates[-1][0] * coordinates[0][1]
answer -= coordinates[-1][1] * coordinates[0][0]
    
print(f'{0.5 * abs(answer):.1f}')