import sys

sys.stdin = open('input.txt','r')

N, F = map(int, input().split())

check = [0]*(N+1)
res = [0]*N
binomial = [1]*N
for i in range(1, N-1):
    binomial[i] = (binomial[i-1]*(N-i))/i
# [1, 3, 3, 1]

def DFS(L, SUM):
    if L==N and SUM==F:
        for r in res:
            print(r, end=' ')
        sys.exit()
    else:
        for i in range(1, N+1):
            if check[i] == 0:
                # use ith number
                check[i] = 1
                # ith number into permutation
                res[L] = i
                DFS(L+1, SUM+res[L]*binomial[L])
                # initialize
                check[i] = 0

DFS(0, 0)