import sys

sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

lst = []
for _ in range(N):
    score, time = map(int, input().split())
    lst.append((score, time))

MAX = 0

# level, score, time
def DFS(L, S, T):
    global MAX
    if T>M:
        return
    if L==N:
        if S>MAX:
            MAX=S
    else:
        # solve
        DFS(L+1, S+lst[L][0], T+lst[L][1])
        # not solve
        DFS(L+1, S, T)

DFS(0, 0, 0)
print(MAX)