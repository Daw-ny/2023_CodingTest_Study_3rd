# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 재귀함수를 이용한 이진수 출력
n = int(input())


def ten_to_two(num, binum):
    # 몫 나머지 출력
    p, q = divmod(num, 2)

    # 몫이 0이면 이진수 출력 아니면 몫을 입력해서 한번 더 진행
    return str(q) + binum if p == 0 else ten_to_two(p, str(q) + binum)


print(ten_to_two(n, ""))
