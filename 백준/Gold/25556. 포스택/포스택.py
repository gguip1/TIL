import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stacks = [[],[],[],[]]

for idx in range(N):
    can_clean = False
    for stack in stacks:
        if stack:
            if stack[-1] < A[idx]:
                stack.append(A[idx])
                can_clean = True
                break
            else:
                continue
        else:
            stack.append(A[idx])
            can_clean = True
            break

    if not can_clean:
        print('NO')
        sys.exit()

print('YES')
