a = [int(s) for s in input().split()]
res=0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]==a[j]:
            res+=1
print(res)