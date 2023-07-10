# module
import sys

# input
# sys.stdin = open("input.txt", "rt")

# K번째 약수
n, k = map(int, input().split())


# 함수 생성
def gcd(x):
    memory = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            memory.append(i)
            if i != x//i:
                memory.append(x//i)
    return sorted(memory)


# 대입
dodoro = gcd(n)
if len(dodoro) < k:
    print(-1)
else:
    print(dodoro[k - 1])
