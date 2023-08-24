import sys
sys.stdin = open('input.txt','r')

N, M = map(int, input().split())

N = [int(n) for n in str(N)]

stack = []

for n in N :
    # if now_item > last_item, last_item pop!
    while stack and M>0 and stack[-1]<n :
        stack.pop()
        M -= 1
    # else
    stack.append(n)

if M!=0 :
    stack = stack[:-M]

for s in stack :
    print(s, end='')