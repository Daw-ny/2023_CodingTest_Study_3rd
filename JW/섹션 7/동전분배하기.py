n=int(input())
arr=[ int(input()) for i in range(n)]

s=1000000

def dfs(L,a,b,c):
  global s
  if L==n:  
    if a > 0 and b >0 and c > 0 and a != b and a != c and b != c:
      #최대 최소 차의 최소값 
      if (max(a,b,c)-min(a,b,c)) < s:
        s=(max(a,b,c)-min(a,b,c))
        
  #한명씩 동전 분배       
  else:
    dfs(L+1,a+arr[L],b,c)
    dfs(L+1,a,b+arr[L],c)
    dfs(L+1,a,b,c+arr[L])

dfs(0,0,0,0)
print(s)
