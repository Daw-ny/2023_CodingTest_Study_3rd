# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 최대 점수 구하기
n, m = map(int, input().split())
classes = []
maxscore = 0
for _ in range(n):
    classes.append(list(map(int, input().split())))


def dfs(idx, scorehap, cnthap):
    if cnthap > m: # 제한시간 초과
        return
      
    if idx == n: # 마지막까지 전부 진행하면 엔드
        global maxscore
        maxscore = max(maxscore, scorehap)
        return
      
    else:
        score, time = classes[idx]
        dfs(idx + 1, scorehap + score, cnthap + time)
        dfs(idx + 1, scorehap, cnthap)


dfs(0, 0, 0)
print(maxscore)
