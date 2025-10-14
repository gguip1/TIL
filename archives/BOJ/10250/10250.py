import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().rstrip().split())
    
    floor = (N - 1) % H + 1
    room = (N - 1) // H + 1
    
    if room < 10:
        print(str(floor) + '0' + str(room))
    else:
        print(str(floor) + str(room))