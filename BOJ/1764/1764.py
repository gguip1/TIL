import sys

N, M = map(int, sys.stdin.readline().strip().split())

N_people = set([sys.stdin.readline().strip() for _ in range(N)])
M_people = set([sys.stdin.readline().strip() for _ in range(M)])

NM_people = list(N_people & M_people)

NM_people.sort()

print(len(NM_people))

for _ in NM_people:
    print(_)
