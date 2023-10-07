arr=[list(map(int,input().split())) for _ in range(10)]

v=[[0]*10 for _ in range(10)]

dx=[0,0]
dy=[-1,1]
c=0


def dfs(L,x,y):
  global c
  if arr[x][y]==2 :
    c=L
  else:
    for j in range(2):
      nx=x+dx[j]
      ny=y+dy[j]
      
      #옆으로 가야하면 옆으로 전진 
      if 0<= nx <10 and 0 <= ny < 10 and v[nx][ny]==0 and arr[nx][ny]>=1 :
        v[nx][ny]=1
        dfs(L,nx,ny)
        v[nx][ny]=0
        break
    else:
      #아님 밑으로 전진 
      if 0 <= x+1 < 10 and 0 <= y < 10 and v[x+1][y]==0 and arr[x+1][y] >=1:
        v[x+1][y]=1
        dfs(L,x+1,y)
        v[x+1][y]=0

for i in range(10):
  if arr[0][i]==1:
    v[0][i]=1
    dfs(i,0,i)
    v[0][i]=0

print(c)
