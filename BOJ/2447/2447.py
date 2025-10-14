import sys
input = sys.stdin.readline
N = int(input())

def function(N):
    if N == 1:
        return ['*']
    
    stars = function(N // 3)
    empty_list = []
    
    for star in stars:
        empty_list.append(star*3)
    for star in stars:
        empty_list.append(star + ' ' * (N // 3) + star)
    for star in stars:
        empty_list.append(star*3)
    
    return empty_list

print('\n'.join(function(N)))