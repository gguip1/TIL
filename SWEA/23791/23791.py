T = int(input())

for _ in range(T):
    N = int(input())
    players = [None] * N
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A_index = 0
    B_index = 0
    
    for __ in range(N):
        while A_index < N and players[A[A_index] - 1] is not None: 
                A_index += 1
        
        if A_index < N:
            players[A[A_index] - 1] = 'A'
            A_index += 1
        
        while B_index < N and players[B[B_index] - 1] is not None:
                B_index += 1
        
        if B_index < N:
            players[B[B_index] - 1] = 'B'
            B_index += 1
    
    for player in players:
        print(player, end='')
    print()