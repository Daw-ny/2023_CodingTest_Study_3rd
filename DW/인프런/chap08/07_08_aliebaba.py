# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 알리바바와 40인의 도둑
n = int(input())
stone = []
dy = [[0]*n for _ in range(n)]
for _ in range(n):
    stone.append(list(map(int, input().split())))

# 7
for i in range(1, n):
    stone[0][i] += stone[0][i-1]
    stone[i][0] += stone[i-1][0]

for i in range(1, n):
    for j in range(1, n):
        stone[i][j] += min(stone[i-1][j], stone[i][j-1])

print(stone[-1][-1])

# 8
def dfs(i, j):
    if dy[i][j] > 0:
        return dy[i][j]
    if i == 0 and j == 0:
        return stone[0][0]
    else:
        if i == 0:
            dy[i][j] = stone[i][j] + dfs(i, j-1)
        elif j == 0:
            dy[i][j] = stone[i][j] + dfs(i-1, j)
        else:
            dy[i][j] = stone[i][j] + min(dfs(i-1, j), dfs(i, j-1))
        return dy[i][j]


print(dfs(n-1, n-1))
