import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

res = [[0]*N for _ in range(N)]

for _ in range(M):
    start, end, distance = map(int, input().split())
    res[start-1][end-1] = distance

for i in range(N):
    for j in range(N):
        print(res[i][j], end=' ')
    print()