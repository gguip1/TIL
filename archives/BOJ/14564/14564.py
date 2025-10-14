import sys
input = sys.stdin.readline

N, M, A = map(int, input().split())

board = [0 for _ in range(N)]
board[A - 1] = M // 2 + 1

for index in range(A, A + (M - (M // 2 + 2)) + 1):
    board[index] = board[index - 1] + 1

for index in range(A):
    board[index] = 

print(board)

while True:
    num = int(input())
    if num == (M // 2 + 1):
        print(0)
        break
    
    