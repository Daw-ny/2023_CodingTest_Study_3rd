arr=[ i for i in range(1,21)]

for j in range(10):
    a,b=map(int,input().split())
    c=arr[a-1:b]
    arr[a-1:b]=c[::-1]
    
print(*arr)
