def fun(x,r):
  if x==1:
    r+='1'
    return print(r[::-1])
  a,b=divmod(x,2)
  if b==0:
    r+='0'
  else:
    r+='1'
  fun(a,r)


n=int(input())
r=''
fun(n,r)
