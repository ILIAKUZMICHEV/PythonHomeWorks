list1=[]
counter=0
print("введите '000' в конце заполнения списка")
while True:
    word=int(input())
    if word!=000:
        list1.append(word)
    else:
        break
for i in range(1,len(list1)-1):
    if list1[i]>list1[i-1] and list1[i]>list1[i+1]:
        counter+=1
print(counter)