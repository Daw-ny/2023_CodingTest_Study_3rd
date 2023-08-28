# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 르세라핌
first = input()
second = input()
dic1 = {}
dic2 = {}
for i, j in zip(first, second):
    if i not in dic1:
        dic1[i] = 1
    else:
        dic1[i] += 1

    if j not in dic2:
        dic2[j] = 1
    else:
        dic2[j] += 1

for k in first:
    if k not in dic2 or dic1[k] != dic2[k]:
        print("NO")
        break
else:
    print("YES")
