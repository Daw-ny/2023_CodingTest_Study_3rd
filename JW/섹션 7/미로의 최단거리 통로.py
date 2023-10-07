from collections import deque
arr=[list(map(int,input().split())) for _ in range(7)]

q=deque()
q.append((0,0))
dx=[-1,1,0,0]
dy=[0,0,-1,1]
arr[0][0]= 2 #1과 0이라 겹치지 말라고 2시작 

while q :
  x,y=q.popleft()


  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    #목적지에 도착할때 까지 전 좌표에 +1 해서 전진 
    if 0<=nx <=6 and 0 <= ny <= 6 and arr[nx][ny] ==0 :
      arr[nx][ny]= arr[x][y]+1
      q.append((nx,ny))

if arr[6][6]==0:
  print(-1)
else:
  print(arr[6][6]-2) 
  #방문 확인을 안 만들고 2부터 시작시켜서 -2 
