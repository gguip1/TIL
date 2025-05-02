import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
count = 0

if N > 0:
    books = list(map(int, sys.stdin.readline().rstrip().split()))

    while len(books) > 0:
        weight = M
        
        while len(books) > 0:
            if books[0] <= weight:
                weight -= books[0]
                books.pop(0)
            else:
                break
        
        count += 1

print(count)

## 최대 효율
# if N > 0:
#     books = list(map(int, sys.stdin.readline().rstrip().split()))
    
#     while len(books) > 0:
#         weight = M
#         greedy = -1
#         greedy_index = -1
#         for index, book in enumerate(books):
#             if greedy < book:
#                 greedy = book
#                 greedy_index = index

#         weight -= greedy
#         books.pop(greedy_index)

#         while len(books) > 0 and weight >= min(books):
#             greedy = -1
#             greedy_index = -1
#             for index, book in enumerate(books):
#                 if book <= weight and greedy < book:
#                     greedy = book
#                     greedy_index = index
#             weight -= greedy
#             books.pop(greedy_index)
        
#         count += 1

# print(count)