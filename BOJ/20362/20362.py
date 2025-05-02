import sys

N, S = sys.stdin.readline().rstrip().split()
N = int(N)

chats = {}
for _ in range(N):
    nick, answer = sys.stdin.readline().rstrip().split() 
    chats[nick] = answer

correct_answer = chats[S]

count = 0

for nick, answer in chats.items():
    if nick == S:
        break
    else:
        if answer == correct_answer:
            count += 1

print(count)
