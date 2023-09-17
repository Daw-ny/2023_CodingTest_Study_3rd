n, m =map(int,input().split())


def dfs(L,lst):
    global CNT
    if L==m:
        print(*lst)
        CNT+=1
        return
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                dfs(L+1,lst+[i])
                ch[i]=0
CNT=0
ch=[0]*(n+1)
dfs(0,[])
print(CNT)
