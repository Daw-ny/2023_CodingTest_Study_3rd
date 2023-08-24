import sys
sys.stdin = open('input.txt','r')

eq = input()

res = ''
stack = []

for e in eq :
    # number
    if e.isdecimal() :
        res += e
    # operators
    else :
        if e == '(' :
            stack.append(e)
        elif e == '*' or e == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                res += stack.pop()
            stack.append(e)
        elif e == '+' or e == '-' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.append(e)
        elif e == ')' :
            while stack and stack[-1] != '(' :
                res += stack.pop()
            stack.pop()

while stack :
    res += stack.pop()

print(res)