# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 사다리 타기
latter = []
for _ in range(10):
    latter.append(list(map(int, input().split())))

q = deque()
for j in range(10):
    if latter[9][j] == 2:
        q.append([9, j])

dx = [0, 0, -1]
dy = [-1, 1, 0]
b = 0
while q:
    a, b = q.popleft()
    for k in range(3):
        x = dx[k] + a
        y = dy[k] + b
        if 0 <= x < 10 and 0 <= y < 10 and latter[x][y] == 1:
            latter[x][y] = 0
            q.append([x, y])
            break # 사다리 타면 다른길로 갈 필요 없음

print(b)
