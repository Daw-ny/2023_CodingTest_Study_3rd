# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 네트워크 선 자르기 (top-down)
n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
dp[2] = 2


def memo(k):
    if dp[k]:
        return dp[k]
    else:
        dp[k] = memo(k-1) + memo(k-2)
        return dp[k]


print(memo(n))
