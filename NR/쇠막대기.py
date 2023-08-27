s = input()

stack=[]
cnt=0
for i in range(len(s)):
    if s[i]==')':
        if s[i-1]=='(':
            stack.pop()
            cnt+=len(stack)
        else:
            stack.pop()
            cnt+=1

    else:
        stack.append(s[i])
print(cnt)
