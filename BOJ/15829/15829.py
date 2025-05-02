r = 31
M = 1234567891

L = int(input())

string = list(input())

sum_ = 0

for index, value in enumerate(string):
    sum_ += (ord(value) - 96) * (r ** (index))

print(sum_ % M)
