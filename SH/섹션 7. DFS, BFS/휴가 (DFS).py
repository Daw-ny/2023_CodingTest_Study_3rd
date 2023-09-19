import sys

sys.stdin = open('input.txt','r')

N = int(input())

lst = [(0, 0)]
for _ in range(N):
    days, pay = map(int, input().split())
    lst.append((days, pay))

MAX = 0

# level, pay
def DFS(L, P):
    global MAX
    # cut edge
    if L>N+1:
        return
    # work until Nth day
    if L==N+1:
        if P>MAX:
            MAX = P
    else:
        # consulting O
        DFS(L+lst[L][0], P+lst[L][1])
        # consulting X
        DFS(L+1, P)

# start from 1st day!
DFS(1, 0)
print(MAX)