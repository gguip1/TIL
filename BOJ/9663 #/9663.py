import sys

N = int(sys.stdin.readline().rstrip())

# 같은 행에는 없다는 조건
def nQuuens(i, col:list):
    n = len(col) - 1
    
    if promising(i, col):
        if n == i:
            print(i, col)
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                nQuuens(i + 1, j)

# 유망한지 체크
def promising(i, col:list):
    if checkColumn(i, col) or checkDiagonal(i, col):
        return False
    return True

# 열 체크
def checkColumn(i, col:list):
    for c in col[1:i]:
        if col[i] == c:
            return False
    return True

# 대각선 체크
def checkDiagonal(i, col:list):
    for key, value in col[1:i]:
        if abs(key - i) == abs(value - col[i]):
            return False
    return True

col = [0] * (N + 1)
nQuuens(0, col)