import sys

A, B, V = map(int, sys.stdin.readline().split())

# if ((V - A) / (A - B) + 1) % int((V - A) / (A - B) + 1) > 0:
#     print((V - A) // (A - B) + 1 + 1) 
# else:
#     print((V - A) // (A - B) + 1)


# 개선
def ceil(num):
    if num == int(num):
        return int(num)
    return int(num) + 1

print(ceil((V - A) / (A - B)) + 1)