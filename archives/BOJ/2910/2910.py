import sys
input = sys.stdin.readline

N, C = map(int, input().split())
messages = list(map(int, input().split()))

messages_dict = {
    
}

for message in messages:
    if messages_dict.get(message) is None:
        messages_dict[message] = 1
    else:
        messages_dict[message] += 1

for key, value in sorted(list(messages_dict.items()), reverse=True, key=lambda x: x[1]):
    print(f'{key} ' * value, end='')
