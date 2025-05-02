T = int(input())

for t in range(T):
    k = int(input()) + 1
    n = int(input())

    floor = []

    for i in range(k):
        room = []
        for j in range(n):
            if i == 0:
                room.append(j + 1)
            else:
                if j == 0:
                    room.append(1)
                else:
                    room.append(floor[i - 1][j] + room[j - 1])
        floor.append(room)

    print(floor[k - 1][n - 1])

