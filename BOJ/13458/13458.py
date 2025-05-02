import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B, C = map(int, sys.stdin.readline().rstrip().split())

viewer = 0

for a in A:
    if a > B:
        viewer += 1
        if (a - B) % C == 0:
            viewer += (a - B) // C
        else:
            viewer += (a - B) // C + 1
    else:
        viewer += 1

print(viewer)
