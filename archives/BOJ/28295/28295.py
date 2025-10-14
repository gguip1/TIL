import sys
input = sys.stdin.readlines
commands = input()

direction = 0
for command in commands:
    if command.strip() == '1':
        direction += 1
    elif command.strip() == '2':
        direction += 2
    elif command.strip() == '3':
        direction -= 1

    if direction < 0:
        direction += 4
        
    direction %= 4

if direction == 0:
    print('N')
elif direction == 1:
    print('E')
elif direction == 2:
    print('S')
elif direction == 3:
    print('W')
        
    