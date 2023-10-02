# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 사과나무
ground = []
for _ in range(7):
    ground.append(list(map(int, input().split())))
q = deque([[0, 0, 0]])
visit = [[0]*7 for _ in range(7)]
visit[0][0] = 1
end = -1
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while q:
    a, b, c = q.popleft()
    if [a, b] == [6, 6]:
        end = c
        break
    for k in range(4):
        x = dx[k] + a
        y = dy[k] + b
        if 0 <= x < 7 and 0 <= y < 7 and visit[x][y] == 0 and ground[x][y] == 0:
            visit[x][y] = 1
            q.append([x, y, c+1])

print(end)
