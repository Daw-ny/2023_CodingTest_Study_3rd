n=int(input())
arr=list(map(int,input().split()))
m=int(input())

arr.sort()

for _ in range(m):
    arr[0]+=1
    arr[-1]-=1
    arr.sort()

print(arr[-1]-arr[0])
