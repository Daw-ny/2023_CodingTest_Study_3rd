import sys
input=sys.stdin.readline

n=int(input())

arr=[]
 
for i in range(n):
    arr.append(list(map(int,input().split())))
    
    
m=int(input())
    
for _ in range(m):
    a,b,c=map(int, input().split())
    if b==0:
        for _ in range(c):
            arr[a-1].append(arr[a-1].pop(0))
            
            
    else:
        for _ in range(c):
            arr[a-1].insert(0,arr[a-1].pop())

            
            
s=0
e=n
result=0
for i in range(n):
    for j in range(s,e):
        result+=arr[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(result)
