import sys; input = sys.stdin.readline

T, N = map(int, input().split())

p_positions = [1] * N
p_inventories = [[] for _ in range(N)]

answer_log = []
answer_pla = []

for _ in range(T):
    log = list(input().split())
    
    match log[2]:
        case 'M':
            p_positions[int(log[1]) - 1] = int(log[3])
        case 'F':
            if p_positions[int(log[1]) - 1] != int(log[3]):
                answer_log.append(int(log[0]))
            p_inventories[int(log[1]) - 1].append(int(log[3]))
        case 'C':
            if int(log[3]) not in p_inventories[int(log[1]) - 1] or int(log[4]) not in p_inventories[int(log[1]) - 1]:
                answer_log.append(int(log[0]))
            if int(log[3]) in p_inventories[int(log[1]) - 1]:
                p_inventories[int(log[1]) - 1].remove(int(log[3]))
            if int(log[4]) in p_inventories[int(log[1]) - 1]:
                p_inventories[int(log[1]) - 1].remove(int(log[4]))
        case 'A':
            if p_positions[int(log[1]) - 1] != p_positions[int(log[3]) - 1]:
                answer_log.append(int(log[0]))
                answer_pla.append(int(log[1]))

print(len(answer_log))
if answer_log:
    print(*sorted(answer_log))
print(len(set(answer_pla)))
if answer_pla:
    print(*sorted(set(answer_pla)))
