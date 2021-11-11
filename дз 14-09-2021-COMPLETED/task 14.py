list1=[]
maks=0
while True:
    word=input()
    if word !="0":
        list1.append(int(word))
    else:
        break
for i in range(0,len(list1)):
    if list1.count(list1[i])!=1:
        if list1.count(list1[i])>maks:
            maks=list1.count(list1[i])
print(maks)
        
