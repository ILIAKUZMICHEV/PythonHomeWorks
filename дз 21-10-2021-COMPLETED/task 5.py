list1 = [ int(s) for s in input().split() ]
for i in range(0,len(list1)):
    if list1.count(list1[i])==1:
        print(list1[i])