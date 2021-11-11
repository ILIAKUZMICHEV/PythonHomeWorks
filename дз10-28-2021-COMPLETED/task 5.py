def power(a,n):
    b=a 
    if n == 0:
        b=1
        return b 
    if n >= 1:
        for i in range(n-1):
            b=b*a 
        return b 
    if n <= (-1):
        n=n*(-1)
        for i in range(n-1):
            b=b*a 
        b=1/b
        return b
print("введите число a")
a=int(input())
print("введите число n")
n=int(input())
print(power(a,n))
        