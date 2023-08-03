arr=[list(map(int, input().split())) for _ in range(7)]
  
    
c=0
for i in range(3):
    for j in range(7):
        if arr[j][i:i+5] == arr[j][i:i+5][::-1]:
            c+=1
        for k in range(2):
            if arr[i+k][j] != arr[i+5-k-1][j]:
                break
        else:
            c +=1
            
print(c)
