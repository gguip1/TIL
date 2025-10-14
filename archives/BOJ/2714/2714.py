import sys
input = sys.stdin.readline
T = int(input())

def convert_to_message(matrix:list):
    message = ''
    top, bottom = 0, int(R) - 1
    left, right = 0, int(C) - 1
    
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            message += matrix[top][c]
        top += 1
        
        for r in range(top, bottom + 1):
            message += matrix[r][right]
        right -= 1
        
        if top <= bottom:
            for c in range(right, left - 1, -1):
                message += matrix[bottom][c]
            bottom -= 1
        
        if left <= right:
            for r in range(bottom, top - 1, -1):
                message += matrix[r][left]
            left += 1
    
    return message    

def convert_to_string(message:str):
    value = 0
    for i in range(5):
        if message[i] == '1':
            value += 2 ** (4 - i)
    if value == 0:
        return ' '
    return chr(64 + value)

for _ in range(T):
    R, C, message = input().split()

    matrix = [[0 for c in range(int(C))] for r in range(int(R))]

    for r_index in range(int(R)):
        for c_index in range(int(C)):
            matrix[r_index][c_index] = message[r_index * int(C) + c_index]    

    message = convert_to_message(matrix)

    answer = ''
    
    string_msg = ''
    
    for m in message:
        if len(string_msg) < 5:
            string_msg += m
        else:
            answer += convert_to_string(string_msg)
            string_msg = m
    
    while len(string_msg) != 0 and len(string_msg) <= 5:
        if len(string_msg) == 5:
            answer += convert_to_string(string_msg)
            break
        string_msg += '0'
    print(answer.rstrip())
