import sys
def dfs(L):
    if L==n:
        a_sum=0
        b_sum=0
        for i in range(len(ch)):
            if ch[i]==1:
                a_sum+=lst[i]
            else:
                b_sum+=lst[i]

        if a_sum==b_sum:
            print('YES')
            sys.exit(0)

    else:
        ch[L]=1
        dfs(L+1)
        ch[L]=0
        dfs(L+1)

n = int(input())
lst = list(map(int, input().split()))
ch=[0]*n
dfs(0)
print('NO')
