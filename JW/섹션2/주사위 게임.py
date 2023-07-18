n=int(input())
min=0

for i in range(n):
    arr=list(map(int,input().split()))
    arr.sort()
    
    if arr[0]==arr[1]==arr[2]:
        s=10000 +(arr[0]*1000)
        
    elif arr[0]==arr[1] or arr[0]==arr[2]:
        s= 1000 + (arr[0]*100)
        
    elif arr[1]==arr[2] :
        s= 1000 +(arr[1]*100)
        
    elif arr[0] != arr[1] != arr[2]:
        s= max(arr)*100
    
    if min < s:
        min= s

print(min)
