import sys

log = []
fix = set()
containers = []
seen = set()

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    log.append(sys.stdin.readline().rstrip())

K = int(sys.stdin.readline().rstrip())

for _ in range(K):
    fix.add(sys.stdin.readline().rstrip())

for l in reversed(log):
    if l in fix and l not in seen:
        containers.append(l)
        seen.add(l)
        fix.remove(l)

for l in reversed(log):
    if l not in seen:
        containers.append(l)
        seen.add(l)

for c in containers:
    print(c)