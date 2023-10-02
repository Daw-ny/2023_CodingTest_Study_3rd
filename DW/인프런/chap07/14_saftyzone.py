# module
import sys
from collections import deque
import copy

# input
#sys.stdin = open("input.txt", "rt")

# 안전영역
n = int(input())
mountain = []
for _ in range(n):
    mountain.append(list(map(int, input().split())))


def checkthesafezone(s, ground, cri): # 외딴섬 몇개인지 카운트
    def bfs(sx, sy, maps): # 외딴섬이 어디까지인지 표시
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        nmap = len(maps)
        maps[sx][sy] = 0
        q = deque([[sx, sy]])
        while q:
            a, b = q.popleft()
            for k in range(4):
                x = dx[k] + a
                y = dy[k] + b
                if 0 <= x < nmap and 0 <= y < nmap and maps[x][y] > cri:
                    maps[x][y] = 0
                    q.append([x, y])

        return maps

    safezone = 0
    for i in range(s):
        for j in range(s):
            if ground[i][j] > cri:
                ground = bfs(i, j, ground)
                safezone += 1

    return safezone


minh = min(sum(mountain, []))
maxh = max(sum(mountain, []))
cnt = 0
for h in range(minh + 1, maxh): # 카운트 한것 중 최대값을 출력
    cnt = max(cnt, checkthesafezone(n, copy.deepcopy(mountain), h))

print(cnt)
