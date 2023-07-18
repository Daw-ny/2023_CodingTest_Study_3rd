n,m=map(int,input().split())

d=dict()
for i in range(1,n+1):
    for j in range(1, m+1):
        if i+j not in d:
            d[i+j]=1
        else:
            d[i+j]+=1

arr=[]
for k in d:
    if d[k]==max(d.values()):
        arr.append(k)

print(*arr)
