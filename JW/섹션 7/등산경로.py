n=int(input())

max=-2000
min=2000000

v=[[0]*n for _ in range(n)]
arr=[]

for i in range(n):
  a=list(map(int,input().split()))
  arr.append(a)

  for j in range(n):
    #가장 낮은 곳 좌표 
    if a[j] < min:
      min=a[j]
      minx=i
      miny=j

    #가장 높은 곳 좌표
    if a[j]> max :
      max= a[j]
      maxx=i
      maxy=j


dx=[-1,1,0,0]
dy=[0,0,-1,1]
c=0
v[minx][miny]=1

def dfs(x,y):
  global c
  #목적지에 도착할때 +1
  if x==maxx and y ==maxy :
    c+=1
  else:
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if 0<= nx <n and 0 <= ny < n and v[nx][ny]==0 and arr[nx][ny] > arr[x][y] :
        v[nx][ny]=1
        dfs(nx,ny)
        v[nx][ny]=0


dfs(minx,miny)
print(c)
