# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 가장 높은 탑 쌓기
n = int(input())
stone = [[1000000, 0, 10000000]]
for _ in range(n):
    stone.append(list(map(int, input().split())))

stone.sort(reverse=True) # 돌에 번호를 붙였다는데 이게 들어가는거 보면 문제 오류일 가능성 매우 높음.
dp = [0] * (n+1)
dp[1] = stone[1][1]
for i in range(2, n+1):
    h = 0
    for j in range(i):
        if stone[i][2] > stone[j][2] or stone[i][0] > stone[j][0]:
            continue
        h = max(h, dp[j])
    dp[i] = h + stone[i][1]

print(max(dp))
