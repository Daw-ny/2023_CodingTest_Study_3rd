n,m=map(int,input().split())
s=[]
t=[]
6
for i in range(n):
  a,b=map(int,input().split())
  s.append(a)
  t.append(b)


def DFS(L, sum, time):
    global res
    if time>m:
      return
    elif L==n:
      if sum > res :
        res=sum
    else:
      DFS(L+1, sum+s[L], time+t[L])
      DFS(L+1, sum, time)

res=0
DFS(0, 0, 0)
print(res)
