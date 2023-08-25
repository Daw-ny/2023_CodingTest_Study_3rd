# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 후위식 연산
Cal = input()
stack = []
for i in Cal:
    if i.isdigit():
        stack.append(i)
    else:
        a = stack.pop()
        b = stack.pop()
        stack.append(str(eval(b+i+a)))
print(*stack)
