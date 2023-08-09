n,m=map(int,input().split())

dvd=list(map(int,input().split()))


def count(x):
    c=1
    s=0
    
    for i in dvd :
        if s+i > x:
            c+=1
            s=i
        else:
            s +=i
    return c

start=dvd[0]
end=sum(dvd)

while start <= end :
    mid=(start+end) //2 

    if count(mid) <= m :
        result=mid
        end=mid-1
        
    else:
        start=mid+1
        
print(result)  
