def DFS(L, x):
    global c
    if L==m:
      print(*r[:m])
      c+=1
    else:
        for i in range(x, n+1):
            r[L]=i
            DFS(L+1, i+1)
           

n, m=map(int, input().split())
r=[0]*(n+1)
c=0
DFS(0, 1)
print(c)
