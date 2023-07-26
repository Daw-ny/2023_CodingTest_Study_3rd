n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))
    
    
sum=[]
di_1=0
di_2=0
for i in range(n):
    row= 0
    col=0
    for j in range(n):
        row += arr[i][j]
        col += arr[j][i]
    sum.append(row)
    sum.append(col)
    di_1+=arr[i][i]
    di_2+=arr[i][n-i-1]
sum.append(di_1)
sum.append(di_2)
        
print(max(sum))
