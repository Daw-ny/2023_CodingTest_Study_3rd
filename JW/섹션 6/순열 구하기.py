def dfs(v):
    global c
    if v==m:
      print(*r[:m])
      c+=1
    else:
        for i in range(1,n+1):
            if arr[i]==0:
                r[v]=i
                arr[i]=1
                dfs(v+1)
                arr[i]=0

n,m=map(int, input().split())
r=[0]*m
arr=[0]*(n+1)
c=0
dfs(0)
print(c)
