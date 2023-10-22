n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    MAX=0
    for j in range(i-1,0,-1):
        if arr[i]>arr[j] and dy[j]> MAX:
            MAX = dy[j]
    dy[i]=MAX+1
    if dy[i]> res:
        res=dy[i]

print(res)