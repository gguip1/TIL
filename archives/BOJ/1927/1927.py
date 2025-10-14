import sys

class Heap():
    def __init__(self):
        self.heap = []
    
    def insert(self, val):
        self.heap.append(val)
        index = len(self.heap) - 1
        parent = ((index - 1) // 2)
        while index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = ((index - 1) // 2)
    
    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        
        return root
    
    def _heapify_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index
        
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def __str__(self):
        return str(self.heap)
    
# Case 2:
N = int(sys.stdin.readline().strip())
heap = Heap()
for i in range(N):
    Q = int(sys.stdin.readline().strip())
    if Q == 0:
        smallest = heap.extract_min()
        if smallest is None:
            print(0)
        else:
            print(smallest)
    else:
        heap.insert(Q)

# Case 1: 시간 초과일듯
# N = int(sys.stdin.readline().strip())
# arr = []
# for i in range(N):
#     Q = int(sys.stdin.readline().strip())
#     if Q == 0 and arr:
#         print(min(arr))
#         arr.remove(min(arr))
#     elif Q == 0 and not arr:
#         print(0)
#     else:
#         arr.append(Q)