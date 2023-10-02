# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 송아지 찾기
s, e = map(int, input().split())

if s > e:
    print(s - e)
elif s == e:
    print(0)
else:
    p, q = divmod(e - s, 5)
    print(p + min(q, 5-q+1))
