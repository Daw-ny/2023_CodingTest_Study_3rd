import sys

sys.stdin = open('input.txt','r')

N = int(input())

result = []

def DFS(x):
    if x == 0:
        return
    else:
        quotient, remainder = divmod(x, 2)
        result.append(remainder)
        DFS(quotient)

DFS(N)

for r in result[::-1]:
    print(r, end='')