import sys
input = sys.stdin.readline

N, L, H = map(int, input().split())
ratings = list(map(int, input().split()))
ratings.sort()

print(sum(ratings[L:N - H]) / len(ratings[L:N - H] ))