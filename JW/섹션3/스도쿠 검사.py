arr=[]


for i in range(9):
    arr.append(list(map(int,input().split())))

    
    
for i in range(9):
    if sorted(arr[i]) != [1,2,3,4,5,6,7,8,9] :
        print('NO')
        break
        
    b= [j[i] for j in arr]
    if sorted(b) != [1,2,3,4,5,6,7,8,9]:
        print('NO')
        break
    
    ab=[]
    if i == 0 or i == 3 or i ==6:
        for k in range(i,i+3):
            c=[arr[k][l] for l in range(i,i+3)]
            ab+=c
            
        if sorted(ab) != [1,2,3,4,5,6,7,8,9] :
            print('NO')
            break
else:
    print('YES')
