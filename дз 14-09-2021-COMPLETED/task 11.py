list1=[]
res=0
print("введите последовательность по одному символу, в конце последовательности напишите 'end'")
while True:
    word=input()
    if word !="end":
        list1.append(word)
    else:
        break
for i in range(0,len(list1)):
    if list1.count(list1[i])==1:
        res+=1
print(res)