import sys
input = sys.stdin.readline

birth = input().strip()
N = int(input())
coding_dates = [input().strip() for n in range(N)]

def calc_year(birth_year, coding_year):
    result = 0
    for i in range(4):
        result += (int(birth_year[i]) - int(coding_year[i])) ** 2
    return result

def calc_month_day(birth_month_day, coding_month_day):
    result = 0
    for i in range(2):
        result += (int(birth_month_day[i]) - int(coding_month_day[i])) ** 2
    return result

def get_coding_bio_rhythm(birth, coding_date):
    birth_year, birth_month, birth_day = birth[:4], birth[4:6], birth[6:]
    coding_year, coding_month, coding_day = coding_date[:4], coding_date[4:6], coding_date[6:]
    
    return calc_year(birth_year, coding_year) * calc_month_day(birth_month, coding_month) * calc_month_day(birth_day, coding_day)

answer = -1
max_value = -1

for coding_date in coding_dates:
    value = get_coding_bio_rhythm(birth, coding_date)
    if answer == -1 and max_value == -1:
        answer = int(coding_date)
        max_value = value
    elif max_value == value:
        answer = min(int(coding_date), answer)
        max_value = value
    elif value > max_value:
        answer = int(coding_date)
        max_value = value

print(answer)
