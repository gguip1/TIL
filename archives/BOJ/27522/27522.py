import sys

scores = [10, 8, 6, 5, 4, 3, 2, 1, 0]

records = []

for _ in range(8):
    record, team = sys.stdin.readline().rstrip().split()
    m, ss, sss = map(int, record.split(':'))
    records.append([team, (m, ss, sss)])

records.sort(key=lambda x: x[1])

Blue = 0
Red = 0

for index, value in enumerate(records):
    team, record = value
    if team == 'B':
        Blue += scores[index]
    else:
        Red += scores[index]

if Blue > Red:
    print('Blue')
else:
    print('Red')