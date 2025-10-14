n = [int(input()) for _ in range(5)]
n.sort()
print(sum(n) // len(n))
print(n[len(n) // 2])