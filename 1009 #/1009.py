T = int(input())

result = []

for i in range(T):
    a, b = map(int, input().split())

    a_10 = a % 10
    
    if a_10 == 0:
        result.append(10)
    elif a_10 == 1 or a_10 == 5 or a_10 == 6:
        result.append(a_10)
    elif a_10 == 2 or a_10 == 3 or a_10 == 7 or a_10 == 8:
        if (b % 4) == 0:
            result.append((a_10 ** 4) % 10)
        else:
            result.append((a_10 ** (b % 4)) % 10)
    elif a_10 == 4 or a_10 == 9:
        if (b % 2) == 0:
            result.append((a_10 ** 2) % 10)
        else:
            result.append(a_10)

for value in result:
    print(value)
