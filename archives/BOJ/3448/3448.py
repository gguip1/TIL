import sys
input = sys.stdin.readline
N = int(input())

R = 0
A = 0

for line in sys.stdin.readlines():
    if line == '\n':
        x10 = (100 * 100 * R) // A         
        x10 = (x10 + 5) // 10   

        whole = x10 // 10
        frac  = x10 % 10
        if frac == 0:
            print(f"Efficiency ratio is {whole}%.")
        else:
            print(f"Efficiency ratio is {whole}.{frac}%.")
        R = 0
        A = 0
    else:
        R += len(line.replace('#', '').rstrip())
        A += len(line.rstrip())
