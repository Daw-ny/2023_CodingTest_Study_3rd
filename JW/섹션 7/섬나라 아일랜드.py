from collections import deque
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
c=0

dx=[-1,1,0,0,-1,1,1,-1] #상하좌우, 대각선
dy=[0,0,-1,1,1,-1,1,-1]

q=deque()
for i in range(n):
  for j in range(n):
    if arr[i][j]==1:
      arr[i][j]=0
      q.append((i,j))
      
      while q :
        x,y=q.popleft()
        for l in range(8):
          nx= x+dx[l]
          ny= y+dy[l]
          
          if 0 <= nx < n and 0 <= ny < n and arr[nx][ny]==1:
            arr[nx][ny]=0
            q.append((nx,ny))
            
      c+=1 #while 끝나면 섬 갯수 +1

print(c)
