from collections import deque

n,m=map(int,input().split())
arr=deque(map(int,input().split()))
arr_index=deque(i for i in range(n))

c=1

while True :

  MAX=max(arr)

  x=arr.popleft()
  y=arr_index.popleft()

  if x == MAX :
    if y==m:
      print(c)
      break
    else:
      c+=1
  else:
    arr.append(x)
    arr_index.append(y)
