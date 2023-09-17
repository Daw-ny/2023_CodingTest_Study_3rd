def DFS(x):
    global c
    if x == n:
    	c+=1
    else:
      for i in range(1, n+1):
        if arr[x][i] == 1 and visit[i] == 0:
          visit[i] = 1
          DFS(i)
          visit[i] = 0



n,m=map(int,input().split())
arr=[[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1	

c = 0
visit = [0]*(n+1)
visit[1] = 1
DFS(1)
print(c)
