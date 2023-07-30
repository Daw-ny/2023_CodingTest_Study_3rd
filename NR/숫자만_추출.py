# s = input()

# n = int(''.join([i for i in s if i.isnumeric() ]))

def divisor(number):
    cnt=0
    for i in range(1, int(number**0.5)+1):
        if number % i==0:
            cnt+=1
        if number**0.5 == i:
            return 2*cnt -1
    return 2*cnt

if __name__=="__main__":
    s = input()
    n = int(''.join([i for i in s if i.isnumeric() ]))
    print(n)
    print(divisor(n))