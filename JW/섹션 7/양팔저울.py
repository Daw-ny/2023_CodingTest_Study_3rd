k=int(input())
arr= list(map(int,input().split()))

res=[0]*(sum(arr)+1)

def dfs(L,a,b):
  global res 
  if res[abs(b-a)]==0:
    res[abs(b-a)]=1
  
  if L==k:
    return 
  
  else:
    dfs(L+1,a,b)
    dfs(L+1,a+arr[L],b)
    dfs(L+1,a,b+arr[L])

dfs(0,0,0)
print(res.count(0))
