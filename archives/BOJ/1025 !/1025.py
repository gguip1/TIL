import sys

N, M = map(int, sys.stdin.readline().strip().split())

table = []
p_square_list = []

for _ in range(N):
    table.append(list(sys.stdin.readline().strip()))

def is_p_square(N):
    if int(N ** 0.5) ** 2 == int(N):
        return True
    else:
        return False

for i in range(N):
    for j in range(M):
        for x in range(-N, N):
            for y in range(-M, M):
                a, b = i, j
                num = ''

                while 0 <= a < N  and 0 <= b < M:
                    if x == 0 and y == 0:
                        break
                    
                    num += table[a][b]
                    
                    if is_p_square(int(num)):
                        p_square_list.append(int(num))
                    
                    a += x
                    b += y
                print(num)

if p_square_list:
    print(max(p_square_list))
else:
    print(-1)