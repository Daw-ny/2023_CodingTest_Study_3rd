from collections import deque


n = int(input())

candidate =[]

for _ in range(n):
    candidate.append(list(map(int,input().split())))


candidate.sort(key = lambda x : (x[0],x[1]), reverse=True)

queue = deque(candidate)
select_h = 0
select_w = 0
cnt = 0
while queue:
    height, weight = queue.popleft()

    if height >= select_h or weight >= select_w:
        select_h = height
        select_w = weight
        cnt+=1

print(cnt)
