N = int(input())

def step(n):
    if n == 1:
        return 1
    else:
        return (n - 1) * 6

value = 0
    
for i in range(N):
    value += step(i + 1)
    
    if value >= N:
        print(i + 1)
        break
