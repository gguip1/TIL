import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    can = True

    current_num = 1

    stack_1 = []
    stack_2 = []

    for a in A:
        if a == current_num:
            current_num += 1
        else:
            if not stack_1:
                if stack_2 and stack_2[-1] == a - 1:
                    stack_2.append(a)
                else:
                    stack_1.append(a)
                continue

            if not stack_2:
                if stack_1 and stack_1[-1] == a - 1:
                    stack_1.append(a)
                else:
                    stack_2.append(a)
                continue
            
            if stack_1 and stack_2:
                if stack_1[-1] == a - 1:
                    stack_1.append(a)
                    continue

                if stack_2[-1] == a - 1:
                    stack_2.append(a)
                    continue
                
                if stack_1[0] == current_num:
                    current_num += len(stack_1)
                    stack_1.clear()
                    stack_1.append(a)
                    continue

                if stack_2[0] == current_num:
                    current_num += len(stack_2)
                    stack_2.clear()
                    stack_2.append(a)
                    continue
                
                can = False
                break

    if can:
        print('YES')
    else:
        print('NO')