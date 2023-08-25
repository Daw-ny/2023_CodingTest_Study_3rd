# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 쇠 막대기
FeBar = input()
stack = []
cnt = 0

for i in range(len(FeBar)):
    if FeBar[i] == '(':
        stack.append(FeBar[i])
    elif FeBar[i - 1] == '(':
        stack.pop()
        cnt += len(stack)
    else:
        stack.pop()
        cnt += 1
print(cnt)
