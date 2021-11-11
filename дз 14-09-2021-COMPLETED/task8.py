list1=[]
counter=0
while True:
    word=int(input())
    if word != 0:
        list1.append(word)
    else:
        list1.append(word)
        break
for i in range(1,len(list1)):
    if list1[i]>list1[i-1]:
        counter+=1
print(counter)
