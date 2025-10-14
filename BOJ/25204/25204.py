import sys
input = sys.stdin.readline

def solve(strings:list):
    for idx_1 in range(len(strings)):
        for idx_2 in range(len(strings)):
            if idx_1 == idx_2:
                continue
            
            str_1_len, str_2_len = len(strings[idx_1]), len(strings[idx_2])
            # if (str_1_len > str_2_len and strings[idx_1][:str_2_len] == strings[idx_1]) or (str_1_len < str_2_len and strings[idx_2][:str_1_len] == strings[idx_2]):
            if (str_1_len < str_2_len and strings[idx_2][:str_1_len] == strings[idx_2]):
                strings[idx_1], strings[idx_2] = strings[idx_2], strings[idx_1]
            else:
                diff_idx = 0
                for idx in range(min(str_1_len, str_2_len)):
                    if strings[idx_1][idx] != strings[idx_2][idx]:
                        diff_idx = idx
                        break
                # if (strings[idx_1][diff_idx] == '-' and strings[idx_2][diff_idx] != '-') or (strings[idx_1][diff_idx] != '-' and strings[idx_2][diff_idx] == '-'):
                if (strings[idx_1][diff_idx] == '-' and strings[idx_2][diff_idx] != '-'):
                    strings[idx_1], strings[idx_2] = strings[idx_2], strings[idx_1]
                else:
                    if (strings[idx_1][diff_idx] != '-' and strings[idx_2][diff_idx] != '-'):
                        
    
    return strings

T = int(input())

for _ in range(T):
    n = int(input())
    print(*solve(list(input().strip() for _ in range(n))), sep='\n')