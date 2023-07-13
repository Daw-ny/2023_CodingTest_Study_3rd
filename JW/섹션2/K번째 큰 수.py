n,k=map(int,input().split())
arr=list(map(int,input().split()))
answer=set()
    
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            answer.add(arr[i]+arr[j]+arr[l])
    
print(sorted(answer,reverse=True)[k-1])
