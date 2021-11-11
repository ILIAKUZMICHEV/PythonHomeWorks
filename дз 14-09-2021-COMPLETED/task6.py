list1=[]
while True:
    word=input()
    if word != "end":
        list1.append(word)
    else:
        break
i=0
for list1[i] in list1:
    if int(list1[i])%2==0:
        print(list1[i])
    i+=1