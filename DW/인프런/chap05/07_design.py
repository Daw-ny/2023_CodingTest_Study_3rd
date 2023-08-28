# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 교육과정 설계
Cri = list(reversed(list(input())))
n = int(input())

for j in range(n):
    Map = input()
    Cong = Cri.copy()
    for i in Map:
        if not Cong:
            break

        elif i in Cong[:-1]:
            break

        if Cong[-1] == i:
            Cong.pop()

    if not Cong:
        print("#%d YES" % (j+1))

    else:
        print("#%d NO" % (j+1))
