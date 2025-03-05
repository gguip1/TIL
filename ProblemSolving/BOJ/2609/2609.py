n1, n2 = map(int, input().split())


def gcd(n1, n2):
    result = 1
    for i in range(min(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            result = i
            return result
    return result

def lcm(n1, n2):
    for i in range(max(n1, n2), n1 * n2 + 1):
        if i % n1 == 0 and i % n2 == 0:
            result = i
            return result

print(gcd(n1, n2))
print(lcm(n1, n2))
