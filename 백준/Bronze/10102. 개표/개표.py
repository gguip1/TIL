A = int(input())
B = input()
v = [0, 0]

for i in range(A):
    if B[i] == 'A':
        v[0] += 1
    else:
        v[1] += 1

if v[0] > v[1]:
    print('A')
elif v[0] < v[1]:
    print('B')
else:
    print('Tie')
