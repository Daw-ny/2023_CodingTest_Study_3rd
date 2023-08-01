# method : BFS

import sys
from collections import deque

sys.stdin = open('input.txt','rt')

N = int(input())

lst = [[0]*N for _ in range(N)]
for i in range(N) :
    row = list(map(int, input().split()))
    for j in range(N) :
        lst[i][j] = row[j]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

check = [[0] * N for _ in range(N)]
cnt = 0
Q = deque()

# initialize : from center
check[N//2][N//2] = 1
cnt += lst[N//2][N//2]
Q.append((N//2, N//2))

# L -> level
L = 0
while True:
    if L == N//2:
        break
    for i in range(len(Q)):
        now = Q.popleft()
        for j in range(4):
            x = now[0] + dx[j]
            y = now[1] + dy[j]
            if check[x][y] == 0:
                cnt += lst[x][y]
                check[x][y] = 1
                Q.append((x, y))
    L += 1

print(cnt)