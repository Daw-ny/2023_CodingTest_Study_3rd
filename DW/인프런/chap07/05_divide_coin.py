# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 동전 분배하기
n = int(input())
coin = []
for _ in range(n):
    coin.append(int(input()))
dab = 10e9


def dfs(idx, first, second, third):
    if idx == n:
        if first == second or second == third or first == third: # 같은 값이 하나라도 존재하면 안됨
            return

        high = max([first, second, third])
        low = min([first, second, third])
        global dab
        dab = min(dab, high-low)
        return

    else:
        dfs(idx + 1, first + coin[idx], second, third)
        dfs(idx + 1, first, second + coin[idx], third)
        dfs(idx + 1, first, second, third + coin[idx])


dfs(0, 0, 0, 0)
print(dab)
