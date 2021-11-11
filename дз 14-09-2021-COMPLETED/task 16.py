v1=[int(s) for s in input().split()]
v2=[int(s) for s in input().split()]
c=0
for i in range(0,len(v1)):
    c+=v1[i]*v2[i]
print(c)