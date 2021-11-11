print("введите рост каждого человека,в конце напишите end")
Heights=[]
while True:
    word=input()
    if word!="end":
        Heights.append(word)
    else:
        break
print("введите рост Пети")
height=int(input())
for i in range(1,len(Heights)):
    if height>int(Heights[i]) and height<int(Heights[i-1]):
        print(i+1)
    if height==int(Heights[i-1]) and height!=int(Heights[i]):
        print("место Пети в строю:",i+1)

