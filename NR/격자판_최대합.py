n = int(input())

graph = []
SUM=0
for i in range(n):
    graph.append(list(map(int, input().split())))

SUM_lst = [sum(graph[i]) for i in range(n)]


for i in range(n):
    for j in range(n):
        SUM+=graph[j][i]

        if j==n-1:
            SUM_lst.append(SUM)
            SUM=0
SUM=0
for i in range(n):
    SUM+=graph[i][i]
SUM_lst.append(SUM)
SUM=0
for i in range(n):
    SUM+=graph[i][n-1-i]
SUM_lst.append(SUM)

print(max(SUM_lst))


                
