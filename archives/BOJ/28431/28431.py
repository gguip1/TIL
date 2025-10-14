socks = []

check = [0 for i in range(10)]

for i in range(5):
    socks.append(int(input()))

for sock in socks:
    check[sock] += 1

for index, value in enumerate(check):
    if value % 2 == 1:
        print(index)
