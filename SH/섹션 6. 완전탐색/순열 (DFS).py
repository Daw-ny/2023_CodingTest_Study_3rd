import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

check = [0]*(N+1)
res = [0]*M
cnt = 0

def DFS(L):
    global cnt
    if L==M:
        # count + 1
        cnt += 1
        # print permutation w/o repitition
        for r in res:
            print(r, end=' ')
        print()
    else:
        for i in range(1, N+1):
            if check[i] == 0:
                # use ith number
                check[i] = 1
                # ith number into permutation
                res[L] = i
                DFS(L+1)
                # initialize
                check[i] = 0

DFS(0)
print(cnt)