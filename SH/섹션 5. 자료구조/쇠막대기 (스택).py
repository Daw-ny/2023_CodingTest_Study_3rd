import sys
sys.stdin = open('input.txt','r')

L = input()

stack = []
cnt = 0

for i in range(len(L)) :
    # (
    if L[i] == '(' :
        stack.append(L[i])
    # )
    else :
        # laser
        if L[i-1] == '(' :
            stack.pop()
            cnt += len(stack)
        # end of stick
        else :
            stack.pop()
            cnt += 1

print(cnt)