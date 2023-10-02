# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 등산경로
n = int(input())
mountain = []
for _ in range(n):
    mountain.append(list(map(int, input().split())))

start = [0, 0]
end = [0, 0]
for i in range(n):
    for j in range(n):
        if mountain[start[0]][start[1]] > mountain[i][j]: # 최저 높이 
            start = [i, j]
        if mountain[end[0]][end[1]] < mountain[i][j]: # 최고 높이
            end = [i, j]

method = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def dfs(a, b):
    if [a, b] == end:
        global method
        method += 1
        return

    for k in range(4):
        x = dx[k] + a
        y = dy[k] + b
        if 0 <= x < n and 0 <= y < n and mountain[x][y] > mountain[a][b]:
            dfs(x, y)


dfs(*start)
print(method)
