# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# K번째 큰 DFS
n, k = map(int, input().split())
numlist = list(map(int, input().split()))
combi = set()


# dfs로 3개 숫자의 합 꺼내기
def dfs(replay, hap, index):
    if replay >= 3:
        combi.add(hap)
        return

    if index < n:
        dfs(replay, hap, index + 1)
        dfs(replay + 1, hap + numlist[index], index + 1)


dfs(0, 0, 0)
print(sorted(combi, reverse=True)[k-1])
