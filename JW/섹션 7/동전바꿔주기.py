t=int(input())
k=int(input())


c1=[]
c2=[]

for i in range(k):
  a,b=map(int,input().split())
  c1.append(a)
  c2.append(b)

c=0

def dfs(L,s):
  global c
  if s > t :
    return 
  if L==k :
    if s==t:
      c+=1
  else:
    for i in range(c2[L]+1):
      dfs(L+1,s+(c1[L]*i))


dfs(0,0)
print(c)
