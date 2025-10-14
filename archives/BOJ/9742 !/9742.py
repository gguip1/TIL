import sys
input = sys.stdin.readlines
cases = input()

def solve(word, string, step, target):
    global now
    
    if step == len(word):
        now += 1
        if now == target:
            return string
    
    for w in word:
        if w not in string:
            q = solve(word, string + w, step + 1, target)
            if q:
                return q
    
    return

for case in cases:
    word, target = case.split()
    target = int(target.strip())
    now = 0
    
    q = solve(word, '', 0, target)
    if q:
        print(f'{word} {target} = {q}')
    else:
        print(f'{word} {target} = No permutation')

# for case in cases:
#     word, target = case.split()
#     target = int(target.strip())
    
#     try:
#         print(f'{word} {target} = ', end='')
#         print(*list(permutations(word))[target - 1], sep='')
#     except:
#         print('No permutation')
