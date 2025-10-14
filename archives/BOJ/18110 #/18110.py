import sys

def round_function(num):
    if num % 1 * 10 >= 5:
        return int(num) + 1
    else:
        return int(num)

# n = int(input())
n = int(sys.stdin.readline().strip())

if n:
    difficulty = []

    for i in range(n):
        # difficulty.append(int(input()))
        difficulty.append(int(sys.stdin.readline().strip()))
    
    except_n = round_function(n * 0.15)
    
    difficulty.sort()
    if except_n != 0:
        difficulty = difficulty[except_n : -except_n]
    print(round_function(sum(difficulty) / len(difficulty)))
else:
    print(0)

# round의 경우 오사오입 사사오입 함수로 동작
# input -> sys.stdin.readline.strip로 변환
