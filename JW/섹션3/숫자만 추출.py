str=input()
num=''
for i in range(len(str)):
    if str[i].isnumeric():
        num += str[i]

num=int(num)
answer=0
for j in range(1,int(num**(1/2))+1):
    if num % j ==0 :
        answer +=1
        if j**2 != num :
            answer +=1
print(num,answer)
