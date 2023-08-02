# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 격자판 회문수
graph = []
for _ in range(7):
    graph.append(input().split())

string_number = []
for r, c in zip(graph, zip(*graph)):
    string_number.append(''.join(r))
    string_number.append(''.join(c))

cnt = 0
for i in string_number:
    for j in range(3):
        num = i[j:j + 5]
        if num == num[::-1]:
            cnt += 1

print(cnt)
