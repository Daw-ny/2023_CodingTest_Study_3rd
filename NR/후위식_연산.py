num = input()

stack=[]
for i in num:

    if i.isnumeric():
        stack.append(int(i))
    else:
        if i=='+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2+n1)
        elif i== '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2-n1)
        elif i== '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2*n1)
        elif i=='/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2/n1)

print(stack[0])
