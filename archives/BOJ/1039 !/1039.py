import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
N = list(str(N))
length = len(N)

queue = []
queue.append((N, 0))
visited = [{} for _ in range(K + 1)]

answer = -1

while queue:
    num, cnt = queue.pop(0)

    if cnt == K:
        val = int(''.join(num))
        answer = max(answer, val)
    else:
        for i in range(length - 1):
            for j in range(i + 1, length):
                num_copy = num.copy()
                num_copy[i], num_copy[j] = num_copy[j], num_copy[i]

                if num_copy[0] == '0':
                    continue

                num_str = ''.join(num_copy)
                if num_str not in visited[cnt + 1]:
                    visited[cnt + 1][num_str] = True
                    queue.append((num_copy, cnt + 1))

print(answer)