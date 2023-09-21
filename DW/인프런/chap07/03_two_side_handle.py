# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 양팔저울
k = int(input())
weight = list(map(int, input().split()))
num = sum(weight)
case = set()


# dfs
def dfs(idx, hap):
    if idx == k:
        if hap > 0:
            case.add(hap)
        return

    else:
        dfs(idx + 1, hap)
        dfs(idx + 1, hap - weight[idx])  # 반대쪽에도 저울을 올리기 가능
        dfs(idx + 1, hap + weight[idx])


dfs(0, 0)
print(num - len(case))
