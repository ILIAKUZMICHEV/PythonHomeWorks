list1=[]
while True:
    word=input()
    if word != "end":
        list1.append(word)
    else:
        break
for i in range(1,len(list1)):
    if (int(list1[i])>=0 and int(list1[i-1])>=0) or (int(list1[i])<0 and int(list1[i-1])<0):
        print(list1[i-1],list1[i])
        break
    