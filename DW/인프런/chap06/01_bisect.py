# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 재귀함수를 이용한 이진수 출력
n = int(input())


def ten_to_two(num, binum):
    p, q = divmod(num, 2)
    return str(q) + binum if p == 0 else ten_to_two(p, str(q) + binum)


print(ten_to_two(n, ""))
