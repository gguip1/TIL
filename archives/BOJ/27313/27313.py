import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
animations = list(map(int, sys.stdin.readline().rstrip().split()))
animations.sort()

animation = []
count = 0

for i in range(N - 1, -1, -1):
    if animations[i] > M:
        continue

    animation.append(animations[i])

    if len(animation) == K:
        max_time = max(animation)
        if max_time <= M:
            M -= max_time
            count += K
            animation = []
        else:
            break

if animation:
    max_time = max(animation)
    if max_time <= M:
        M -= max_time
        count += len(animation)

print(count)