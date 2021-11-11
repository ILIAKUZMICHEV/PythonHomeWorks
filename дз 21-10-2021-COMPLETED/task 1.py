a=input().split()
print(a)
k=input()
count=a.count(k)
while count>0:
    a.remove(k)
    count-=1
print(a)