S = list(input())

result = [-1 for _ in range(26)]

for index, value in enumerate(S):
    if result[ord(value) - 97] == -1:
        result[ord(value) - 97] = index

for index, value in enumerate(result):
    print(value, end=" ")
