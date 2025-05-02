num = input()

if len(num) == 2:
    print(int(num[0]) + int(num[1]))
elif len(num) == 3:
    for index, value in enumerate(list(num)):
        if value == '0':
            if index > 1:
                print(int(num[index - 2]) + int(num[index - 1] + num[index]))
            else:
                print(int(num[index + 1]) + int(num[index - 1] + num[index]))
            break
else:
    print(20)
