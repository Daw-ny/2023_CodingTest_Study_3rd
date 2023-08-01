# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 사과나무
n = int(input())
middle = n//2
graph = []
hap = 0
for _ in range(n):
    ls = list(map(int, input().split()))
    graph.append(ls)

for i in range(middle+1):
    hap += sum(graph[i][middle-i:middle+i+1])

for j in range(middle):
    hap += sum(graph[n-j-1][middle-j:middle+j+1])

print(hap)
