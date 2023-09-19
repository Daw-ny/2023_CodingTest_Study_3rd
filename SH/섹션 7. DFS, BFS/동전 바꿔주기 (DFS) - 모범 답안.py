import sys

sys.stdin = open('input.txt','r')

T = int(input())
K = int(input())
lst = []
for _ in range(K):
    p, n = map(int, input().split())
    lst.append((p, n))

cnt = 0

# L : how many coins you use?
# S : sum
def DFS(L, S):
    global cnt
    if S>T:
        return
    # I've considered all K coins
    if L==K:
        if S==T:
            cnt += 1
    else:
        # I'll use 0 Lth coin ~ ni Lth coin
        for i in range(lst[L][1]+1):
            DFS(L+1, S+lst[L][0]*i)

DFS(0, 0)
print(cnt)