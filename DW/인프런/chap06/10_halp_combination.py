# module
import sys
sys.setrecursionlimit(10**9)

# input
#sys.stdin = open("input.txt", "rt")

# 조합 구하기
n, m = map(int, input().split())
p = 0


# dfs
def dfs(cnt, num, lst):
    if num > n+1: # num이 5일때 4가 들어가는 경우도 있음 따라서 여기까지 돌려줘야 마무리 가능
        return

    if cnt == m:
        print(*lst)
        global p
        p += 1
        return

    else:
        lst.append(num)
        dfs(cnt + 1, num + 1, lst)
        lst.pop() # 백트래킹
        dfs(cnt, num + 1, lst)


dfs(0, 1, [])
print(p)
