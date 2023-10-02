# module
import sys
from itertools import combinations
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 피자 배달 거리
n, m = map(int, input().split())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 여기 하나 차이로 case3이 pass/time limit exceed
# for _ in range(n):
#    path.append(list(map(int, input().split())))

pizza = []
for c in range(n): # 피자 지점 확보
    for j in range(n):
        if path[c][j] == 2:
            pizza.append([c, j])

mindistance = 10e8
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
for c in combinations(pizza, m):
    q = deque(c)
    road = [[-1]*n for _ in range(n)]
    for t in c: # 피자집부터 출발하므로 거리는 0으로 채워줌
        road[t[0]][t[1]] = 0
    d = 0
    while q:
        a, b = q.popleft()
        if path[a][b] == 1:
            d += road[a][b]
            if d >= mindistance: # 최소를 넘으면 그만돌림
                break
            else:
                continue # 최소를 넘기지 않으면 계속 돌림

        for k in range(4):
            x = dx[k] + a
            y = dy[k] + b
            if 0 <= x < n and 0 <= y < n and (road[x][y] == -1 or road[x][y] > road[a][b] + 1): # 최소거리가 아니거나 거리측정 안했으면 실행
                road[x][y] = road[a][b] + 1
                q.append([x, y])

    mindistance = min(mindistance, d)

print(mindistance)
