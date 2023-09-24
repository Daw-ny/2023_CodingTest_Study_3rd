n=int(input())
t=[]
p=[]

for i in range(n):
  a,b=map(int,input().split())
  t.append(a)
  p.append(b)


def dfs(time,point):
  global res
  if time==n:
    if point >res:
      res=point
  else:
    if time+t[time] <= n:
      dfs(time+t[time],point+p[time])
    dfs(time+1,point)

res=0
dfs(0,0)
print(res)
