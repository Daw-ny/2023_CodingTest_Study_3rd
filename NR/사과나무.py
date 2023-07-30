from collections import deque
n = int(input())


graph=[]

for i in range(n):
    graph.append(list(map(int, input().split())))


dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = [[0]*5 for _ in range(n)]

def bfs(x,y):

    queue = deque()
    cnt=0
    queue.append((x,y, cnt))
    visited[x][y] =1
    SUM =0 
    SUM += graph[x][y]

    while queue:

        x, y , cnt = queue.popleft()

        if cnt== n//2:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < n and 0<=ny < n:
                if visited[nx][ny]==0:
                    visited[nx][ny]=1
                    SUM+=graph[nx][ny]
                    queue.append((nx,ny, cnt+1))

    return SUM
print(bfs(2,2))
