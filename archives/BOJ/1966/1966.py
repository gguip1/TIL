import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().strip().split()))
    
    answer = 0
    
    while True:
        node = queue.pop(0)
        is_print = True
        
        for index in range(len(queue)):
            if queue[index] > node:
                queue.append(node)
                is_print = False
                break
        
        if is_print:
            answer += 1

        if is_print and M == 0:
            print(answer)
            break

        M = (M - 1) if (M - 1) >= 0 else len(queue) - 1
    