n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
    

s=0

for i in range(n//2+1):
    
    if i== n //2 :
        s += sum(arr[i])
    else:
        s+= sum(arr[i][n//2-i:n//2+i+1])
        s+= sum(arr[n-1-i][n//2-i:n//2+i+1])
        
print(s)
