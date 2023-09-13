# module
import sys
sys.setrecursionlimit(10**9)

# input
#sys.stdin = open("input.txt", "rt")

# 수들의 조합
n, k = map(int, input().split())
intiger = list(map(int, input().split()))
m = int(input())
a = 0


# dfs
def dfs(idx, hap, cnt):
    global a
    if idx == n: # 마지막 숫자를 넘어갔을때 바로 판독
        if cnt == k:
            if hap % m == 0:
                a += 1
        return

    if cnt == k: # 도중에 만족했을 때 판독
        if hap % m == 0:
            a += 1
        return

    else:
        hap += intiger[idx]
        dfs(idx + 1, hap, cnt + 1)
        hap -= intiger[idx] # 백트래킹
        dfs(idx + 1, hap, cnt)


dfs(0, 0, 0)
print(a)
