import sys

sys.stdin = open('input.txt','r')

N = int(input())
coins = list(map(int, input().split()))
M = int(input())

# initialize cnt
cnt = M+1
# sort descending -> exchange w/ larger values first
coins.sort(reverse=True)

def DFS(L, SUM):
    global cnt
    # cut edge
    if L >= cnt:
        return
    if SUM > M:
        return
    if SUM == M:
        if L < cnt:
            cnt = L
    else:
        for i in range(N):
            DFS(L+1, SUM+coins[i])

DFS(0, 0)
print(cnt)