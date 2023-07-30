n = int(input())

lst1 = list(map(int, input().split()))

m = int(input())

lst2 = list(map(int, input().split()))

lst = lst1 + lst2
lst = sorted(lst)

print(*lst)