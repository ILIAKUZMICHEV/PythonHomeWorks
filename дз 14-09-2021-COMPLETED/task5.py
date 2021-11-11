list1=[]
while True:
    word=input()
    if word !="end":
        list1.append(word)
    else:
        break
list2=[]
for i in range(0,len(list1)):
    if i%2==0:
        list2.append(list1[i])
print(list2)