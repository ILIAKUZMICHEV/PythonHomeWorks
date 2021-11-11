n=int(input())
nod=n
for i in range(2,n):
    if (i < nod) and (n % i == 0):
        nod=i
print(nod)

