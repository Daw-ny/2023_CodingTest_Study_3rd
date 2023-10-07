n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
a=[]

dx=[-1,1,0,0]
dy=[0,0,-1,1]



def dfs(x,y):
  global c
  c+=1 
  arr[x][y]=0
  for l in range(4):
    nx=x+dx[l]
    ny=y+dy[l]
    if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]==1 :
      dfs(nx,ny)



for i in range(n):
  for j in range(n):
    if arr[i][j]==1:
      c=0
      dfs(i,j)
      a.append(c)


a.sort()
print(len(a))

for k in a:
  print(k)
