from collections import deque

required = input()
n = int(input())


for i in range(n):

    plan = input()
    queue = deque(required)
    for p in plan:
        if p in queue:
            if p !=queue.popleft():
                print('#{} NO'.format(i+1))
                break


    else:
        if len(queue)==0:
            print('#{} YES'.format(i+1))
        else:
            print('#{} NO'.format(i+1))
