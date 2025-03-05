import sys

# def conquer_z(arr):
#     if len(arr) <= 1:
#         return arr
    
#     col_mid = len(arr) // 2
#     row_mid = len(arr[0]) // 2
    
#     first_arr = conquer_z(arr[:col_mid][:row_mid])
#     second_arr = conquer_z(arr[col_mid:][:row_mid])
#     third_arr = conquer_z(arr[:col_mid][row_mid:])
#     fourth_arr = conquer_z(arr[col_mid:][row_mid:])
    
#     return merge_z(first_arr, second_arr, third_arr, fourth_arr)

# def merge_z(first_arr, second_arr, third_arr, fourth_arr):
#     result = []
    
#     result.extend(first_arr)
#     result.extend(second_arr)
#     result.extend(third_arr)
#     result.extend(fourth_arr)
    
#     return result

index = 0

def conquer_z(N):
    global index
    
    if N == 0:
        index += 1
        return index
    
    first_arr = conquer_z(N - 1)
    second_arr = conquer_z(N - 1)
    third_arr = conquer_z(N - 1)
    fourth_arr = conquer_z(N - 1)
    
    return merge_z(first_arr, second_arr, third_arr, fourth_arr)

def merge_z(first_arr, second_arr, third_arr, fourth_arr):
    result = [[],[]]
    
    result[0].append(first_arr)
    result[0].append(second_arr)
    result[1].append(third_arr)
    result[1].append(fourth_arr)
    
    print(result)
    
    return result

N, r, c = map(int, sys.stdin.readline().strip().split())

print(conquer_z(N))
