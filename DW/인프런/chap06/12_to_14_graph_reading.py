# module
import sys

# input
# sys.stdin = open("input.txt", "rt")

# 인접행렬
n, m = map(int, input().split())
graph = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    i, j, k = map(int, input().split())
    graph[i-1][j-1] = k

for a in range(n):
    print(*graph[a])
