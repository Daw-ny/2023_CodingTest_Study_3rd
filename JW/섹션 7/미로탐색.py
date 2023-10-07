arr=[list(map(int,input().split())) for _ in range(7)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
c=0
arr[0][0]=1

def dfs(x,y):
  global c
  
  #좌표에 도착할떄 마다 +1 
  if x==6 and y ==6 :
    c+=1
    
  else:
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      
      if 0<= nx <=6 and 0 <= ny <= 6 and arr[nx][ny] ==0 :
        arr[nx][ny]=1
        dfs(nx,ny)
        arr[nx][ny]=0


dfs(0,0)
print(c)
