# module
import sys
sys.setrecursionlimit(10**9)

# input
#sys.stdin = open("input.txt", "rt")

# 순열 구하기
n, m = map(int, input().split())
cnt = 0
num = [0]*n


# dfs
def dfs(idx, lst):
    global cnt
    if idx == m: # 
        print(*num[:m])
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if i in lst: # 안에 숫자 있으면 다음으로 넘김
                continue
            lst[idx] = i
            dfs(idx + 1, lst)
            lst[idx] = 0 # 백트래킹 안하면 숫자가 for문에 의해 겹칠 때가 있음 : 직접 함수에 대입하는거 아니면 기록이 남기 때문에 항상 백트래킹 해줘야함


dfs(0, num)
print(cnt)
