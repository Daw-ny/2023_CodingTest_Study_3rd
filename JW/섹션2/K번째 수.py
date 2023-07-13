x=int(input())
for i in range(x):
    n,s,e,k=map(int,input().split())
    arr=list(map(int,input().split()))     
    print("#%d %d" % (i+1,sorted(arr[s-1:e])[k-1]))
