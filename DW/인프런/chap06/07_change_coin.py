# module
import sys
sys.setrecursionlimit(10**9)

# input
#sys.stdin = open("input.txt", "rt")

# 동전 교환
n = int(input())
coin = sorted(list(map(int, input().split())), reverse=True) # 이거 안뒤집으면 시간초과나서 못함
change = int(input())
mincnt = 10**9


# 거스름돈 경우 확인 dfs
def dfs(cnt, hap):
    global mincnt
    if cnt >= mincnt: # 최저보다 작거나 같아지면 끝
        return

    if hap > change: # 합이 일정 금액보다 넘어가면 끝
        return

    elif hap == change: # 합과 같으면 비교후 끝
        if cnt < mincnt:
            mincnt = cnt
        return

    else:
        for i in coin: # 백트래킹 할거 없이 바로 집어넣으면 순차적으로 대입한거랑 같아짐
            dfs(cnt + 1, hap + i)


# 마무리
if n == 1:
    print(change // coin[0])
else:
    dfs(0, 0)
    print(mincnt)
