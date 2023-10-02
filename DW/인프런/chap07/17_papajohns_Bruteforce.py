# module
import sys
from itertools import combinations

# input
#sys.stdin = open("input.txt", "rt")

# 피자 배달 거리
n, m = map(int, input().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# for _ in range(n):
#    path.append(list(map(int, input().split())))
c = [[i, j] for i in range(n) for j in range(n) if a[i][j] == 2]
h = [[i, j] for i in range(n) for j in range(n) if a[i][j] == 1]

c_list = list(combinations(c, m))


def cal_d(home, place):
    min_dist = 1e9  # 1e9 = 1*10^9

    for ch in place: # 간단하게 계산
        dist = abs(ch[0] - home[0]) + abs(ch[1] - home[1])
        min_dist = min(min_dist, dist)

    return min_dist


b = []
for i in c_list: # 반복문 두번 돌리고 끝
    t = 0
    for j in h:
        t += cal_d(j, i)
    b.append(t)

print(min(b))
