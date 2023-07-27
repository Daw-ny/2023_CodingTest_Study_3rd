n=int(input())
for i in range(n):
    s=input()
    if s.lower()==s[::-1].lower():
        print('#%d' % (i+1), 'YES' )
    else:
        print('#%d' % (i+1), 'NO')
