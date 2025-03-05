import sys

Score_Sum, Score_Sub = map(int, sys.stdin.readline().strip().split())

Team_A = (Score_Sum + Score_Sub) // 2
Team_B = Score_Sum - Team_A

if Team_A + Team_B == Score_Sum and Team_A - Team_B == Score_Sub and Score_Sum >= Score_Sub:
    print(Team_A, Team_B)
else:
    print(-1)
