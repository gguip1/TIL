import heapq
import sys
input = sys.stdin.readline
N = int(input())

for x in range(N):
    T = int(input())
    NA, NB = map(int, input().split())
    NA_times = [tuple(input().split()) for _ in range(NA)]
    NB_times = [tuple(input().split()) for _ in range(NB)]
    
    events = []
    
    for time in NA_times:
        s_time, e_time = time
        s_HH, s_MM = map(int, s_time.split(':'))
        e_HH, e_MM = map(int, e_time.split(':'))
        
        events.append((s_HH * 60 + s_MM, e_HH * 60 + e_MM, 'A'))
    
    for time in NB_times:
        s_time, e_time = time
        s_HH, s_MM = map(int, s_time.split(':'))
        e_HH, e_MM = map(int, e_time.split(':'))
        
        events.append((s_HH * 60 + s_MM, e_HH * 60 + e_MM, 'B'))
    
    events.sort()
    
    a_heap = []
    b_heap = []
    a_answer = 0
    b_answer = 0
    
    for start, end, team in events:
        if team == 'A':
            if b_heap and b_heap[0] <= start:
                heapq.heappop(b_heap)
            else:
                a_answer += 1
            heapq.heappush(a_heap, end + T)
        else:
            if a_heap and a_heap[0] <= start:
                heapq.heappop(a_heap)
            else:
                b_answer += 1
            heapq.heappush(b_heap, end + T)
    
    print(f'Case #{x + 1}: {a_answer} {b_answer}')