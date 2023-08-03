n = int(input())


graph=[]
for i in range(n):
    graph.append( list(map(int, input().split())))


m = int(input())

for i in range(m):
    a,b,c = map(int, input().split())

    if b==0:
        cnt = 0
        while cnt < c:
            tmp = graph[a-1].pop(0)
            graph[a-1].append(tmp)
            cnt+=1
    else:
        cnt=0
        while cnt <c :
            tmp = graph[a-1].pop()
            graph[a-1].insert(0,tmp)
            cnt+=1
print(graph)
i =0
j = n
k =0
answer = 0
while k < n:

    answer += sum(graph[k][i:j])
    if k< n//2:
        i+=1
        j-=1
        k+=1
    else:
        i-=1
        j+=1
        k+=1

print(answer)
