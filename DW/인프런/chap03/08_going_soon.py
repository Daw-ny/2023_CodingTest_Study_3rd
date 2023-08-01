# module
import sys
from collections import deque

# input
#sys.stdin = open("input.txt", "rt")

# 곳감
n = int(input())
graph = []
for _ in range(n):
    graph.append(deque(list(map(int, input().split()))))

m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if b == 0:
        for _ in range(c):
            graph[a-1].append(graph[a-1].popleft())

    else:
        for _ in range(c):
            graph[a-1].appendleft(graph[a-1].pop())

middle = n//2
hap = 0
for i in range(middle):
    cnt = 0
    while cnt < i:
        graph[i].popleft()
        graph[i].pop()
        graph[n - i - 1].popleft()
        graph[n - i - 1].pop()
        cnt += 1
    hap += sum(graph[i])
    hap += sum(graph[n - i - 1])
print(hap + graph[middle][middle])
