# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 에라토스테네스의 체
n = int(input())


# 함수로 만들어버리기
def eratosthenes(x):
    check = [0, 0] + [1] * (x - 1)
    for i in range(2, int(x**0.5) + 1):
        if check[i] == 0:
            continue
        for j in range(i+i, x+1, i):
            check[j] = 0

    return sum(check)


print(eratosthenes(n))
