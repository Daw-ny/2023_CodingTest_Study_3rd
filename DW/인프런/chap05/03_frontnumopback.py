# module
import sys

# input
#sys.stdin = open("input.txt", "rt")

# 후위 표기식 만들기
dic = {'+': 1, '-': 1, '*': 2, '/': 2}
stack = []
Cal = input()
n = ''

for i in Cal:
    if i.isdigit():
        n += i
    elif i == "(":
        stack.append(i)
    elif i == ")":
        while stack and stack[-1] != "(":
            n += stack.pop()
        stack.pop()
    elif i in dic:
        while stack and stack[-1] != "(" and (dic[i] <= dic[stack[-1]]):
            n += stack.pop()
        stack.append(i)

while stack:
    n += stack.pop()

print(n)
