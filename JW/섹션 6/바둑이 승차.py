c,n= map(int,input().split())
arr=[int(input()) for _ in range(n)]
max_val=0

def dfs(i,kg):
    global max_val

    if kg > c:
        return 
    
    if i==n:
        if kg <= c :
            max_val= max(max_val,kg)
        return
    
    else:
        dfs(i+1,kg+arr[i])
        dfs(i+1,kg)

if sum(arr) <= c:
    print(sum(arr))
else:
    dfs(0,0)
    print(max_val)
