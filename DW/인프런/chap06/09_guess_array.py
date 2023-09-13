# module
import sys
sys.setrecursionlimit(10**9)

# input
#sys.stdin = open("input.txt", "rt")

# 수열 추측하기
n, f = map(int, input().split())
result = []


# 파스칼의 삼각형은 (x+c)^n과 같은 계수를 가진다.
def coef(intiger):
    lst = [1]
    for i in range(2, intiger + 1): # 개수에 맞춰서 계수를 만들어 주는 형식으로 진행
        lst = [0] + lst + [0]
        lst = [i + j for i, j in zip(lst[:-1], lst[1:])]

    return lst


# 여기서 dfs를 활용하자
c = coef(n)
num = [a for a in range(n, 0, -1)]


# dfs
def dfs(idx, hap, lst):
    if idx > n: # idx가 n보다 크면 성립안됨
        return

    if hap > f: # 합이 f보다 크면 필요 없음
        return

    elif hap == f: # 합이 f고 idx가 정확히 n개여야 조건에 성립
        if idx == n:
            global result
            result.append(lst.copy()) # 카피 안하면 안담김
        return

    else:
        for k in num:
            if k in lst: # 겹치면 안됨
                continue
            lst.append(k)
            dfs(idx + 1, hap + k*c[idx], lst) # 합 반영
            lst.pop() # 백트래킹 


dfs(0, 0, [])
print(*sorted(result)[0])
