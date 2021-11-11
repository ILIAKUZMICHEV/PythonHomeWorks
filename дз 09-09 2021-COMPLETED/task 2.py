a=int(input())
d=1
while a%10>0:
    d=d*(a%10)
    a=a//10
print(d)
  