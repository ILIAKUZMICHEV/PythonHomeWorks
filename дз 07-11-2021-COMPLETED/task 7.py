x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
kx = abs(x1 - x2)
ky = abs(y1 - y2)
if kx == 1 and ky == 2 or kx == 2 and ky == 1:
    print('YES')
else:
    print('NO')