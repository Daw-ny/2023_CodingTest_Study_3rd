# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 사과나무
n = int(input())
ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))
  
s = n // 2
q = deque([[s, s, 0]])
visit = [[0]*n for _ in range(n)]
visit[s][s] = 1
apple = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while q:
    a, b, c = q.popleft()
    apple += ground[a][b]
    if c < s:
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < n and 0 <= y < n and visit[x][y] == 0:
                visit[x][y] = 1
                q.append([x, y, c+1])

print(apple)
