def makeTable(pattern:list):
    patternSize = len(pattern)
    table = [0] * patternSize
    
    j = 0
    for i in range(1, patternSize):
        while(j > 0 and pattern[i] != pattern[j]):
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    
    return table

def kmp(parent:list, pattern:list):
    parentSize = len(parent)
    patternSize = len(pattern)
    table = makeTable(pattern)
    
    count = 0
    result = []
    
    j = 0
    for i in range(parentSize):
        while(j > 0 and parent[i] != pattern[j]):
            j = table[j - 1]
        if parent[i] == pattern[j]:
            if j == patternSize - 1:
                count += 1
                result.append(i - patternSize + 2)
                j = table[j]
            else:
                j += 1

    return count, result

import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

count, result = kmp(T, P)

print(count)
print(*result)

# T = input()
# P = input()

# count, result = kmp(T, P)

# print(count)
# print(*result)