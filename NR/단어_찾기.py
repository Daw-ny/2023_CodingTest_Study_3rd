n = int(input())


lst = []

for i in range(n):
    lst.append(input())


for i in range(n-1):

    w = input()

    if w in lst:
        lst.remove(w)

print(*lst)
