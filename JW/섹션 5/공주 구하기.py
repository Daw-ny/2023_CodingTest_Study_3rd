from collections import deque

n,k=map(int, input().split())
arr=[i for i in range(1,n+1)]
arr=deque(arr)
c=1

while len(arr)>1:
    if c<k:
        arr.append(arr.popleft())
        c+=1
    else:
        arr.popleft()
        c=1
print(arr[0])
