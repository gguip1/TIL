import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    a, b, S = map(int, input().split())
    
    bigger_a = False
    bigger_b = False
    
    if a > b:
        bigger_a = True
    else:
        bigger_b = True
    
    found = False
    
    if bigger_a:
        for x in range(min(a, S // b + 1)):
            if (S - b * x) % a == 0:
                y = (S - b * x) // a
                if y >= 0:
                    print(y, x)
                    found = True
                    break
    
    if bigger_b:
        for x in range(min(b, S // a + 1)):
            if (S - a * x) % b == 0:
                y = (S - a * x) // b
                if y >= 0:
                    print(x, y)
                    found = True
                    break
    
    if not found:
        print('Impossible')

# for _ in range(T):
#     a, b, S = map(int, input().split())
    
#     bigger_a = False
#     bigger_b = False
    
#     if a > b:
#         bigger_a = True
#     else:
#         bigger_b = True
    
#     a_count = 0
#     b_count = 0
    
#     if bigger_a:
#         a_count = S // a + 1
        
#         while a_count * a + b_count * b != S and a_count >= 0:
#             a_count -= 1
            
#             if (S - a_count * a) % b == 0:
#                 b_count = (S - a_count * a) // b
    
#     if bigger_b:
#         b_count = S // b + 1
        
#         while a_count * a + b_count * b != S and b_count >= 0:
#             b_count -= 1
#             if (S - b_count * b) % a == 0:
#                 a_count = (S - b_count * b) // a
    
#     if a_count < 0 or b_count < 0:
#         print('Impossible')
#     else:
#         print(a_count, b_count)
                
