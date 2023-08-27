x=list(input())

number=[]

for i in x :
  if i.isnumeric():
    number.append(int(i))
  else:
    if i=='+':
      a=number.pop()
      b=number.pop()
      number.append((a+b))

    if i=='-':
      a=number.pop()
      b=number.pop()
      number.append((b-a))
      
    if i=='*':
      a=number.pop()
      b=number.pop()
      number.append((a*b))
      
    if i=='/':
      a=number.pop()
      b=number.pop()
      number.append((b/a))

print(*number)
