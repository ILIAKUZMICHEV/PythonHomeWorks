num=int(input())
txt={}
for i in range(num):
    stroka=input().split()
    for word in stroka:
        txt[word]=txt.get(word,0)+1
print(txt)
print(max(txt.values()))
