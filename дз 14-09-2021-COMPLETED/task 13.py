list1=[]
while True:
    word=input()
    if word !="0":
        list1.append(int(word))
    else:
        break
print(list1.count(max(list1)))