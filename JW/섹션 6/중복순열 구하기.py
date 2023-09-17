def dfs(x):
  global c
  if x==m:
    print(*r)
    c+=1
  else:
    for i in range(1,n+1):
      r[x]=i
      dfs(x+1)

n,m=map(int,input().split())
r=[0]*m
c=0
dfs(0)
print(c)
