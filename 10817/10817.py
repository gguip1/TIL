A, B, C = map(int, input().split())

first = A

if B > first:
    first = B
    second = A
else:
    second = B

if C > first:
    third = second
    second = first
    first = C
else:
    if C > second:
        third = second
        second = C

print(second)
