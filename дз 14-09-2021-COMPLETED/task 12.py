list1=[]
while True:
    word=input()
    if word !="end":
        list1.append(int(word))
    else:
        break
print("max","  ","index")
print(max(list1)," ",list1.index(max(list1)))