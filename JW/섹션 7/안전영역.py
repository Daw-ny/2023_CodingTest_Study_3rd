import sys
sys.setrecursionlimit(10**7) #dfs 풀다가 깊이 안댐 ,, 

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

m=-1


def dfs(x,y,k):
  v[x][y]=1
  for l in range(4):
    nx=x+dx[l]
    ny=y+dy[l]
    if 0 <= nx < n and 0 <= ny < n and v[nx][ny]==0 and arr[nx][ny] > k :
      dfs(nx,ny,k)



#arr의 최대값에 도달할때 까지 낮은 높이부터 for (1~MAX)
for k in range(1,max(max(arr))):
  v=[[0]*n for _ in range(n)]
  c=0
  for i in range(n):
    for j in range(n):
      #방문하지 않고 높이가 k보다 높으면 dfs (잠기지 않음)
      if v[i][j]==0 and arr[i][j]> k :
        c+=1
        dfs(i,j,k)
  m=max(m,c) 

print(m)
