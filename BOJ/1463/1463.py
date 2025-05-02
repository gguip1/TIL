import sys

N = int(sys.stdin.readline().strip())

answer = [0 for _ in range(1000000)]

for i in range(1000000):
    case_a = None
    case_b = None
    
    if (i + 1) == 1:
        answer[i] = 0
        continue
    
    if (i + 1) % 2 == 0:
        case_a = answer[(i + 1) // 2 - 1] + 1
        
    if (i + 1) % 3 == 0:
        case_b = answer[(i + 1) // 3 - 1] + 1
    
    case_c = answer[i - 1] + 1
    
    if case_a is not None and case_b is not None:
        answer[i] = min(case_a, case_b, case_c)
    elif case_a is not None and case_b is None:
        answer[i] = min(case_a, case_c)
    elif case_a is None and case_b is not None:
        answer[i] = min(case_b, case_c)
    else:
        answer[i] = case_c

print(answer[N - 1])