# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 최대 부분 증가 수열
n = int(input())
lst = list(map(int, input().split()))
k = [0]

for i in lst:
    for j in range(1, len(k)):
        if i < k[0]:
            break

        elif k[j-1] < i <= k[j]:
            k[j] = i
            break
    else:
        k.append(i)

print(len(k) - 1)
