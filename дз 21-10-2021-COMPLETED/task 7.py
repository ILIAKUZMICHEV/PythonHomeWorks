a=[int(s) for s in input().split()]
num=int(input())
for i in range(num+1, len(a)):
    a[i-1]=a[i]
a.pop()
print(a)
