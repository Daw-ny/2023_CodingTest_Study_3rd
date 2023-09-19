import sys

sys.stdin = open('input.txt','r')

N = int(input())
coins = list(map(int, input().split()))
M = int(input())

# all 1 won
MIN = M

def DFS(L, C):
    global MIN
    # cut edge
    if C > MIN:
        return
    # exchanging coins finish!
    if L==0:
        if C < MIN:
            MIN = C
    # exchanging coins
    else:
        for i in range(N):
            if L >= coins[i]:
                DFS(L-coins[i], C+1)

DFS(M, 0)

print(MIN)

