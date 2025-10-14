import sys

L = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()

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

print(L - makeTable(S)[-1])
