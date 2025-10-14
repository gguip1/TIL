import sys

counter = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0,
        'G': 0,
        'H': 0,
        'I': 0,
        'J': 0,
        'K': 0,
        'L': 0,
        'M': 0,
        'N': 0,
        'O': 0,
        'P': 0,
        'Q': 0,
        'R': 0,
        'S': 0,
        'T': 0,
        'U': 0,
        'V': 0,
        'W': 0,
        'X': 0,
        'Y': 0,
        'Z': 0,
    }

nums = {
    0: list('ZERO'),
    1: list('ONE'),
    2: list('TWO'),
    3: list('THREE'),
    4: list('FOUR'),
    5: list('FIVE'),
    6: list('SIX'),
    7: list('SEVEN'),
    8: list('EIGHT'),
    9: list('NINE'),
}

def checkCounter(counter:dict):
    for key, value in counter.items():
        if value < 0:
            return False
    return True

def checkCounter_ZWUXG(counter:dict):
    result = []
    for i in range(counter['Z']):
        result.append(0)
        counter['Z'] -= 1
        counter['E'] -= 1
        counter['R'] -= 1
        counter['O'] -= 1
    for i in range(counter['W']):
        result.append(2)
        counter['T'] -= 1
        counter['W'] -= 1
        counter['O'] -= 1
    for i in range(counter['U']):
        result.append(4)
        counter['F'] -= 1
        counter['O'] -= 1
        counter['U'] -= 1
        counter['R'] -= 1
    for i in range(counter['X']):
        result.append(6)
        counter['S'] -= 1
        counter['I'] -= 1
        counter['X'] -= 1
    for i in range(counter['G']):
        result.append(8)
        counter['E'] -= 1
        counter['I'] -= 1
        counter['G'] -= 1
        counter['H'] -= 1
        counter['T'] -= 1
        
    return result

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    S = list(sys.stdin.readline().rstrip())
    result = []
    
    S_counter = counter.copy()
    for s in S:
        S_counter[s] += 1
        
    result.extend(checkCounter_ZWUXG(S_counter))
    
    check_index = 0
    while check_index < 10:
        s_num = nums[check_index]
        S_counter_copy = S_counter.copy()
        
        for s in s_num:
            S_counter_copy[s] -= 1
        
        if checkCounter(S_counter_copy):
            S_counter = S_counter_copy.copy()
            result.append(check_index)
        else:
            check_index += 1
    
    result.sort()
    
    print(f'Case #{_ + 1}: ', end='')
    for r in result:
        print(r, end='')
    print()
