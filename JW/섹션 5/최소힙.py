import heapq

heap=[]

while True :
  x=int(input())
  if x== -1 :
    break
  elif x==0:
    print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, x)
