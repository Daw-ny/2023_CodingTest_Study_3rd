import sys
sys.stdin = open('input.txt', 'rt')

N = int(input())

for i in range(N):
    string = input()
    reverse = string[::-1]
    if string == reverse:
        print('#%d YES' %(i+1))
    else :
        print('#%d NO' %(i+1))