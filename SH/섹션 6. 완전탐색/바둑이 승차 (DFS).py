import sys

sys.stdin = open('input.txt','r')

C, N = map(int, input().split())

dogs = []
for _ in range(N):
    dogs.append(int(input()))

check = [0]*N
MAX = 0

def DFS(x):
    global MAX
    if x==N:
        SUM = 0
        for i in range(N):
            if check[i] == 1:
                SUM += dogs[i]
        # cut edge
        if SUM > C:
            return
        if C >= SUM and SUM >= MAX:
            MAX = SUM
    else:
        # in truck
        check[x] = 1
        DFS(x+1)
        # out truck
        check[x] = 0
        DFS(x+1)

DFS(0)

print(MAX)