n = int(input())

coin= list(map(int,input().split()))

m = int(input())

def dfs(SUM, CNT):
    global MIN
    if CNT > MIN:
        return 
    if SUM > m:
        return

    if SUM==m:
        if CNT < MIN:
            MIN=CNT
    else:
        for i in range(0,n):
            dfs(SUM+coin[i],CNT+1)
    return MIN
MIN=9999999
coin.sort(reverse=True)
print(dfs(0,0))
