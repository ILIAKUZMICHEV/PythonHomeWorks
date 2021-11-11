def bank(a,years):
    while years>0:
        a=float(a*0.1)+a
        years-=1
    return a
a=float(input())
years=int(input())
print(bank(a,years))