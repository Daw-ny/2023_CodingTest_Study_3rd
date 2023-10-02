# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 단지번호 붙이기
n = int(input())
ground = []
for _ in range(n):
    ground.append(list(map(int, input())))


def bfs(sx, sy, maps, numbering):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    nmap = len(maps)
    maps[sx][sy] = numbering
    q = deque([[sx, sy]])
    cnt = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < nmap and 0 <= y < nmap and maps[x][y] == 1:
                maps[x][y] = numbering
                cnt += 1
                q.append([x, y])

    return cnt if cnt != 0 else 1, maps


num = 2
danji = 0
hosu = []
for i in range(n):
    for j in range(n):
        if ground[i][j] == 1:
            ho, ground = bfs(i, j, ground, num)
            danji += 1
            num += 1
            hosu.append(ho)

print(danji)
for z in range(danji):
    print(sorted(hosu)[z])
