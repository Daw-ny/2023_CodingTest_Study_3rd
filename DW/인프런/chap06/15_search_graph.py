# module
import sys
from collections import defaultdict

# input
#sys.stdin = open("input.txt", "rt")

# 인접행렬
n, m = map(int, input().split())
graph = defaultdict(list)
cnt = 0
v = [0]*(n+1)
v[1] = 1
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)


# dfs
def dfs(node, visit):
    if node == n: # 마지막 노드에 도달하면 종료
        global cnt
        cnt += 1
        return

    else:
        for k in graph[node]:
            if visit[k] == 0: # 방문하지 않은 노드만 방문하자
                visit[k] = 1 # dfs함수 안에서 계산 안할경우 백트래킹은 무조건 해야함
                dfs(k, visit)
                visit[k] = 0 # 백트래킹


dfs(1, v)
print(cnt)
