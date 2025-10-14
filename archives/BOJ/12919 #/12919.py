import sys

S = list(sys.stdin.readline().rstrip())
T = list(sys.stdin.readline().rstrip())

def function(string_list):
    if string_list == S:
        return True
    if len(string_list) < len(S):
        return False
    
    if string_list[-1] == 'A':
        if function(string_list[:-1]):
            return True
    if string_list[0] == 'B':
        if function(string_list[1:][::-1]):
            return True
    
    return False

if function(T):
    print(1)
else:
    print(0)

## TLE
# def function(string_list):
#     if len(T) == len(string_list):
#         return T == string_list
    
#     return (
#         function(string_list + ['A']) or
#         function(list(reversed(string_list + ['B'])))
#     )

# if function(S):
#     print(1)
# else:
#     print(0)
