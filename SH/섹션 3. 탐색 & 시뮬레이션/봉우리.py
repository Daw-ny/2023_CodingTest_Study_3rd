import sys
sys.stdin = open('input.txt','rt')

N = int(input())

lst = [[0]*N for _ in range(N)]
for i in range(N) :
    row = list(map(int, input().split()))
    for j in range(N) :
        lst[i][j] = row[j]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0

for i in range(N) :
    for j in range(N) :
        center = lst[i][j]
        for k in range(4) :
            new_x = i+dx[k]
            new_y = j+dy[k]
            if 0<=new_x<N and 0<=new_y<N :
                side = lst[new_x][new_y]
                if side >= center :
                    break
        else :
            cnt += 1

print(cnt)