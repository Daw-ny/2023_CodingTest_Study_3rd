from collections import deque
n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]

sum=arr[n//2][n//2]
arr[n//2][n//2] = -1
q=deque()
q.append((n//2,n//2))
c=0

dx=[-1,1,0,0]
dy=[0,0,-1,1]

while True :
  if c== n//2:
    break

  for i in range(len(q)):
    x=q.popleft()

    #상하좌우로 퍼지게 만들기 
    for j in range(4):
      nx=x[0]+dx[j]
      ny=x[1]+dy[j]

      if arr[nx][ny] != -1 :
        sum+= arr[nx][ny]
        arr[nx][ny] = -1 
        q.append((nx,ny))
  c+=1

print(sum)
