# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 토마토
c, r = map(int, input().split())
tomato = []
for _ in range(r):
    tomato.append(list(map(int, input().split())))

q = deque()
for i in range(r):
    for j in range(c):
        if tomato[i][j] == 1:
            q.append([i, j, 0])

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
day = 0
while q:
    a, b, day = q.popleft()
    for k in range(4):
        x = dx[k] + a
        y = dy[k] + b
        if 0 <= x < r and 0 <= y < c and tomato[x][y] == 0:
            tomato[x][y] = 1
            q.append([x, y, day + 1])

if 0 in sum(tomato, []):
    print(-1)
else:
    print(day)
