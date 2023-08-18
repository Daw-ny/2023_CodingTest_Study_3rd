from collections import deque
n = int(input())
timetable = []
for _ in range(n):
    timetable.append(list(map(int, input().split())))

timetable.sort(key = lambda x : ( x[1], x[0]))

queue = deque(timetable)
cnt=0
e=0
while queue:
    start, end = queue.popleft()

    if e <= start:
        cnt+=1
        e = end

print(cnt)
