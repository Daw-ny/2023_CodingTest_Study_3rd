from collections import deque

n, m = map(int, input().split())

lst1 = list(map(int, input().split()))
lst2 = list(map(lambda x,y : (x, y) ,lst1, [i for i in range(n)]))

queue1 = deque(lst1)
queue2 = deque(lst2)
cnt=0
while True:

    patient ,idx= queue2.popleft()
    patient_ = queue1.popleft()

    if patient < max(queue1):
        queue2.append((patient, idx))
        queue1.append(patient_)

    else:
        cnt+=1
        if idx==m:
            break
print(cnt)
