N = int(input())
T_size_p = list(map(int, input().split()))
T, P = map(int, input().split())

T_order = 0

for _ in T_size_p:
    if _ % T == 0:
        T_order += _ // T
    else:
        T_order += _ // T + 1

print(T_order)
print(sum(T_size_p) // P, sum(T_size_p) % P)
