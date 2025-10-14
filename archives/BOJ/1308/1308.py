import sys
input = sys.stdin.readline

def is_leaf_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

y, m, d = map(int, input().split())
d_y, d_m, d_d = map(int, input().split())

if (d_y == y + 1000 and d_m >= m and d_d >= d) or (d_y > y + 1000):
    print('gg')
    sys.exit()

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leaf_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

answer = 0

if y == d_y:
    if m == d_m:
        answer += d_d - d
    else:
        if is_leaf_year(y):
            answer += leaf_days[m - 1] - d
        else:
            answer += days[m - 1] - d
        for month in range(m + 1, d_m):
            if is_leaf_year(y):
                answer += leaf_days[month - 1]
            else:
                answer += days[month - 1]
        answer += d_d
else:
    for month in range(m, 13):
        if m == month:
            if is_leaf_year(y):
                answer += leaf_days[month - 1] - d
            else:
                answer += days[month - 1] - d
        else:
            if is_leaf_year(y):
                answer += leaf_days[month - 1]
            else:
                answer += days[month - 1]
    for year in range(y + 1, d_y):
        if is_leaf_year(year):
            answer += 366
        else:
            answer += 365
    for month in range(1, d_m + 1):
        if d_m == month:
            answer += d_d
        else:
            if is_leaf_year(d_y):
                answer += leaf_days[month - 1]
            else:
                answer += days[month - 1]

print(f'D-{answer}')
