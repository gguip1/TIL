import sys

class stack:
    def __init__(self, arr:list = []):
        self.arr = arr
    
    def insert(self, value):
        self.arr.append(value)
    
    def pop(self):
        if self.arr:
            return self.arr.pop(len(self.arr) - 1)
        else:
            return -1
    
    def __len__(self):
        return len(self.arr)
    
    def isEmpty(self):
        if not self.arr:
            return 1
        else:
            return 0
    
    def top(self):
        if self.arr:
            return self.arr[len(self.arr) - 1]
        else:
            return -1

N = int(sys.stdin.readline().rstrip())

s = stack()

for i in range(N):
    Q = list(map(int, sys.stdin.readline().rstrip().split()))
    
    if Q[0] == 1:
        s.insert(Q[1])
    elif Q[0] == 2:
        print(s.pop())
    elif Q[0] == 3:
        print(len(s))
    elif Q[0] == 4:
        print(s.isEmpty())
    elif Q[0] == 5:
        print(s.top())
    