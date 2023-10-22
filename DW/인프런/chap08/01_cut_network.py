# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 네트워크 선 자르기 (bottom-up)
n = int(input())
dp = [0] * (n+1)
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
