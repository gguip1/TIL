import sys

def lan_amount(lan_line, size):
    amount = 0
    for lan in lan_line:
        amount += lan // size
    return amount

K, N = map(int, sys.stdin.readline().strip().split())

lan_line = []

for i in range(K):
    lan_line.append(int(sys.stdin.readline().strip()))

amount = lan_amount(lan_line, (max(lan_line) // 2))

if amount == N:
    print()