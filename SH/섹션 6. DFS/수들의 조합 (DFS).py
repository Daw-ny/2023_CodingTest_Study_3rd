import sys

sys.stdin = open('input.txt','r')

N, K = map(int, input().split())
lst = list(map(int, input().split()))
M = int(input())

res = [0]*K
cnt = 0

def DFS(L, S):
    global cnt
    if L==K:
        SUM = 0
        for r in res:
            SUM += r
        if SUM % M == 0:
            cnt += 1
    else:
        for i in range(S, N):
            res[L] = lst[i]
            DFS(L+1, i+1)

DFS(0, 0)
print(cnt)