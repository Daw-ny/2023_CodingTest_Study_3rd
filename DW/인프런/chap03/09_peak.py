# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 봉우리
n = int(input())
graph = [[0] * (n + 2)]
for _ in range(n):
    lst = list(map(int, input().split()))
    graph.append([0] + lst + [0])
graph.append([0] * (n + 2))

mount = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] > graph[i - 1][j] and graph[i][j] > graph[i + 1][j] and graph[i][j] > graph[i][j - 1] and graph[i][j] > graph[i][j + 1]:
            mount += 1

print(mount)
