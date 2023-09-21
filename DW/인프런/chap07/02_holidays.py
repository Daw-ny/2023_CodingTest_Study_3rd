# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 휴가
n = int(input())
consult = []
for _ in range(n):
    consult.append(list(map(int, input().split())))
maxpay = 0


# dfs
def dfs(idx, rest, pay):
    if idx == n:
        global maxpay
        maxpay = max(maxpay, pay)
        return

    if rest != 0:  # 상담기간 안끝나서 바로 다음진행
        dfs(idx+1, rest-1, pay)

    else:
        if n - idx >= consult[idx][0]: # 이 예시를 문제에서 언급을 안한다고?
            dfs(idx + 1, rest + consult[idx][0] - 1, pay + consult[idx][1])
        dfs(idx + 1, rest, pay)


dfs(0, 0, 0)
print(maxpay)
