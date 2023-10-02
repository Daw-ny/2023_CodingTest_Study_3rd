# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 섬나라 아일랜드
n = int(input())
ground = []
for _ in range(n):
    ground.append(list(map(int, input().split())))


def bfs(sx, sy, maps): # 대각선 방향까지 확인
    dx = [0, 0, -1, 1, 1, 1, -1, -1]
    dy = [-1, 1, 0, 0, 1, -1, 1, -1]
    nmap = len(maps)
    maps[sx][sy] = 0
    q = deque([[sx, sy]])
    while q:
        a, b = q.popleft()
        for k in range(8):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < nmap and 0 <= y < nmap and maps[x][y] == 1:
                maps[x][y] = 0
                q.append([x, y])

    return maps


island = 0
for i in range(n):
    for j in range(n):
        if ground[i][j] == 1:
            ground = bfs(i, j, ground)
            island += 1

print(island)
