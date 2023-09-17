n, m = map(int, input().split())

def dfs(L,lst):
    global CNT
    if L==m:
        print(*lst)
        CNT+=1
        return

    else:
        for i in range(1,n+1):
            dfs(L+1,lst+[i])

    return
CNT=0
dfs(0,[])
print(CNT)
