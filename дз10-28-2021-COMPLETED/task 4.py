def distance(x1,x2,y1,y2):
    length=((x2-x1)**2+(y2-y1)**2)**0.5
    return length
x1=float(input())
y1=float(input())
x2=float(input())
y2=float(input())
print(distance(x1,x2,y1,y2))
