print("введите число n")
n=int(input())
while n>1440:
    n=n-1440
print("на циферблате электронных часов время"," ",n//60,":",n%60)
