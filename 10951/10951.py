result = []

while True:
    try:
        A, B = map(int, input().split())
        result.append(A + B)
    except:
        break

for index, value in enumerate(result):
    print(value)
