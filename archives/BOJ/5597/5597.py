p = []
f = []

for i in range(28):
    p.append(int(input()))

for i in range(30):
    if i + 1 in p:
        continue
    else:
        f.append(i + 1)

for i in f:
    print(i)
