a=[int(s) for s in input().split()]
a.append(0)
index=int(input())
num=int(input())
for i in range(len(a)-1,index,-1):
    a[i]=a[i-1]
a[index]=num
print(a)
