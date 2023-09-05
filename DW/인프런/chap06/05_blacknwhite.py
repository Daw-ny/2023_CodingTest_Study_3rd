# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 바둑이 승차
c, n = map(int, input().split())
lst = []
blackandwhite = 0
for _ in range(n):
    lst.append(int(input()))
total = sum(lst)


def dfs(index, weight, rest):
    global blackandwhite
    if weight + rest < blackandwhite: # 앞으로 남은 것들을 다 더해도 완성 안되면 ㅃㅇ
        return

    if weight > c: # 제한 무게 초과하면 ㅃㅇ
        return

    elif index == n: # 반복문 다돌아갔을 때 최대 근접값보다 작으면 ㅃㅇ
        if blackandwhite < weight:
            blackandwhite = weight

    else: # 조건 충족 안됐을 때 다시 한번 재귀문 실행
        dfs(index + 1, weight + lst[index], rest - lst[index])
        dfs(index + 1, weight, rest - lst[index])


dfs(0, 0, total)
print(blackandwhite)
