def is_prime(a):
    k=0
    flag=False
    for i in range(1,a+1):
        if a%i==0:
            k+=1
    if k==2:
        flag=True
    return flag
a=int(input())
print(is_prime(a))
        
        