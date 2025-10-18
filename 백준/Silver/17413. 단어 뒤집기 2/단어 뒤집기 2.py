from collections import deque
import sys
input = sys.stdin.readline

S = input().strip()

word = []
answer = []
tag = False

for s in S:
    if s == '<':
        tag = True
        word.append(s)
    elif s == '>':
        tag = False
        word.append(s)
        answer.append(''.join(word))
        word = []
    elif not tag and s == ' ':
        answer.append(''.join(word) + ' ')
        word = []
    else:
        if tag:
            word.append(s)
        else:
            word.insert(0, s)

if word:
    answer.append(''.join(word))

print(*answer, sep='')
