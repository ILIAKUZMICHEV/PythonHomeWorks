list1=[int(s) for s in input().split()]
set1=set()
for i in list1:
    if i in set1:
        print(i,'-Yes')
    else:
        set1.add(i)
        print(i,'-No')
        