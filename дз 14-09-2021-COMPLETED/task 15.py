a=[int(s) for s in input().split()]
b=[int(s) for s in input().split()]
c=[]
if len(a)>len(b):
    for i in range(len(a)-len(b)):
        b.append(0)
if len(a)<len(b):
    for i in range(len(b)-len(a)):
        a.append(0)
for j in range(0,len(a)):
    c.append(a[j]+b[j])
print(c)
  
        