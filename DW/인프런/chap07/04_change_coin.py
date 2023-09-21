# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 동전바꿔주기
t = int(input())
k = int(input())
coin = []
for _ in range(k):
    coin.append(list(map(int, input().split())))
cnt = 0
coin.sort(key=lambda x: -x[0]) # 큰 동전부터하면 속도가 빠름
total = sum(list(map(lambda x: x[1]*x[0], coin)))


#dfs
def dfs(idx, hap, rest):
    if hap == t: # 딱맞음
        global cnt
        cnt += 1
        return

    if idx == k: # 모자랍
        return

    if hap > t: # 이미 환전하려는 값을 넘어버림
        return

    if hap + rest < t: # 남은걸로도 환전 못함
        return

    else:
        price, p = coin[idx]
        for i in range(p+1):
            dfs(idx+1, hap+price*i, rest-price*p)


dfs(0, 0, total)
print(cnt)
