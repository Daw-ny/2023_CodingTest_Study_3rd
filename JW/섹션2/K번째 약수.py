s,n=map(int,input().split())
answer=[]
for i in range(1,s+1):
    if s % i ==0 :
        answer.append(i)
if len(answer) < n :
    print(-1)
else:
    print(answer[n-1])
