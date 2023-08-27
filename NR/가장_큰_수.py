s, n = input().split()
stack=[]
cnt=0
for i in range(len(s)):
    while stack and s[stack[-1]] < s[i] and cnt<int(n):
        stack.pop()
        cnt+=1
    stack.append(i)
if cnt!=int(n): ########## 중요
    stack=stack[:-cnt]
for i in stack:
    print(s[i], end='')
