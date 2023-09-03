from heapq import heapify, heappop, heappush

heap = []
for i in range(100000):

    n = int(input())
    if n==-1:
        break
    if n==0:
        try:
            print(heappop(heap))
        except:
            print(-1)
            sys.exit(0)
    else:
        heappush(heap,n)
