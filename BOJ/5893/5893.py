import sys

N = sys.stdin.readline().strip()

def bin2dec(num):
    result = 0
    bin_ = 1
    for i in range(len(num) - 1, -1, -1):
        result += int(num[i]) * bin_
        bin_ *= 2
    return result

print(bin(bin2dec(N) * 17)[2:])
