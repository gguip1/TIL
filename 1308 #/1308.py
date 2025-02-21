import sys

def is_leaf_year(year):
    leaf_year = False
    if year % 4 == 0:
        leaf_year = True
        if year % 100 == 0:
            leaf_year = False
            if year % 400 == 0:
                leaf_year = True

    return leaf_year

year, month, day = map(int, sys.stdin.readline().strip().split())
d_year, d_month, d_day = map(int, sys.stdin.readline().strip().split())

if d_year >= year + 1000 and d_month >= month and d_day >= day:
    print('gg')
else:
    days = 0
    
    if year == d_year:
        
        if is_leaf_year(year):
            month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if month == d_month:
            days = d_day - day
        else:
            days += month_day[month - 1] - day
            for m in range(month, d_month):
                days += month_day[m - 1]
            days += d_day
    else:
        for y in range(year, d_year + 1):
            if is_leaf_year(y):
                month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            
            if y == year:
                days += month_day[month - 1] - day
                for m in range(month, 12):
                    days += month_day[m]
            elif y == d_year:
                for m in range(0, d_month - 1):
                    days += month_day[m]
                days += d_day
            else:
                days += sum(month_day)

    print(f'D-{days}')
