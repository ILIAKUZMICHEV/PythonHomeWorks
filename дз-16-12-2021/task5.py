number = int(input())
set1 = set()
for i in range(0, number):
    set1.update(str(s) for s in input().split())
print(len(set1))