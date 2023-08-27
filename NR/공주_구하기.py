from collections import deque
n, m = map(int,input().split())

queue = deque([i for i in range(1,n+1)])

cnt=0

while queue:
    if len(queue)==1:
        break
    q = queue.popleft()
    cnt+=1

    if cnt==m:
        cnt=0
    else:
        queue.append(q)

print(list(queue)[0])
