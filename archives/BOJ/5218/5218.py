import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    words = list(sys.stdin.readline().rstrip().split())
    
    answer = []
    for i in range(len(words[0])):
        answer.append((ord(words[1][i]) - ord(words[0][i])) % 26)
    
    print(f'Distances:', end=' ')
    print(*answer)