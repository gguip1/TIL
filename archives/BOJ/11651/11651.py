import sys
input = sys.stdin.readline

N = int(input().rstrip())
coordinates = [list(map(int, input().rstrip().split())) for x in range(N)]

coordinates.sort()
coordinates.sort(key=lambda coordinate : (coordinate[1]))

for coordinate in coordinates:
    print(coordinate[0], coordinate[1])
