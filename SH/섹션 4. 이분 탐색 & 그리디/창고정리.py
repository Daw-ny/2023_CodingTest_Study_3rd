import sys
sys.stdin = open('input.txt','rt')

L = int(input())
lst = list(map(int, input().split()))
M = int(input())

lst.sort()

for _ in range(M) :
    lst[-1] -= 1
    lst[0] += 1
    lst.sort()

print(lst[-1]-lst[0])