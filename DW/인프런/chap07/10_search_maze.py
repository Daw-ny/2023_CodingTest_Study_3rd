# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 미로탐색
ground = []
for _ in range(7):
    ground.append(list(map(int, input().split())))
ground[0][0] = 1
method = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(a, b):
    if [a, b] == [6, 6]:
        global method
        method += 1
        return

    for k in range(4):
        x = dx[k] + a
        y = dy[k] + b
        if 0 <= x < 7 and 0 <= y < 7 and ground[x][y] == 0:
            ground[x][y] = 1
            dfs(x, y)
            ground[x][y] = 0


dfs(0, 0)
print(method)
