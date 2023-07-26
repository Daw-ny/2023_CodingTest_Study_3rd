n,m=map(int,input().split())
arr=list(map(int,input().split()))

c=0
for i in range(n):
    sum=arr[i]
    if sum == m :
        c +=1 
        
    else:
        for j in range(i+1,n):
            sum +=arr[j]
            
            if sum==m :
                c +=1
                break
                
            elif sum > m :
                break
print(c)
