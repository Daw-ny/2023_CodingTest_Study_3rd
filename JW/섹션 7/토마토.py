from collections import deque 


n,m=map(int,input().split())

arr=[]
for _ in range(m):
  arr.append(list(map(int,input().split())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
day=0

for i in range(m):
  for j in range(n):
    #토마토 좌표 추가 
    if arr[i][j]==1 :
      q.append((i,j))


while q :
  x,y=q.popleft()
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<= nx <m and 0<= ny < n :
      if arr[nx][ny]==0:
        arr[nx][ny]=arr[x][y]+1 #전날 +1일
        q.append((nx,ny))


for i in range(m):
  for j in range(n):
    if arr[i][j]==0:
      print(-1)
      exit()
    day=max(day,arr[i][j])

print(day-1)
