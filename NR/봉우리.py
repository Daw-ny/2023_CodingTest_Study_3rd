n = int(input())
board=[list(map(int,input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer=0
for i in range(n):
    for j in range(n):
        cnt=0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]<board[i][j]:
                    cnt+=1
            else:
                cnt+=1
        if cnt==4:
            answer+=1
print(answer)
