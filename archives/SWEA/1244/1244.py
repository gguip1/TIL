T = int(input())

for _ in range(T):
    num, chance = input().split()
    chance = int(chance)
    length = len(num)
    
    if length == 1:
        print(num)
        continue
    
    queue = [(list(str(num)), 0)]
    visited = [{} for _ in range(chance + 1)]
    answer = -1
    
    while queue:
        val, cnt = queue.pop(0)
        
        if cnt == chance:
            answer = max(answer, int(''.join(val)))
        else:
            for i in range(length - 1):
                for j in range(i + 1, length):
                    val_copy = val.copy()
                    val_copy[i], val_copy[j] = val_copy[j], val_copy[i]
                    
                    val_str = ''.join(val_copy)
                    if val_str not in visited[cnt + 1]:
                        visited[cnt + 1][val_str] = True
                        queue.append((val_copy, cnt + 1))

    print(f'#{_ + 1} {answer}')