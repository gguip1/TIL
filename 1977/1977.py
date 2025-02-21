M = int(input())
N = int(input())

result = []

def perfect_square_number(num):
    for i in range(num + 1):
        if i ** 2 > num:
            return False
        
        if i ** 2 == num:
            return True

for i in range(M, N + 1):
    if perfect_square_number(i):
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)
