n = int(input())

ware = list(map(int, input().split()))


m = int(input())

while m>0:
    ware.sort(reverse=True)
    state = ware.pop(0)

    while state >= ware[0]:
        if m>0:
            m-=1
            state-=1
            ware[-1]+=1
            ware.sort(reverse=True)
        else:
            break
    ware.append(state)
ware.sort(reverse=True)

print(ware[0]-ware[-1])
