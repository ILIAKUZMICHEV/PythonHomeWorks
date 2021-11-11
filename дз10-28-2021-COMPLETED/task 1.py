def srsum(array):
    Summ=0
    for i in range(0,len(array)):
        Summ=Summ+array[i]
    srsum=Summ/len(array)
    return srsum
array=[]
while True:
    word=input()
    if word != "end":
        array.append(float(word))
    else:
        break
print(srsum(array))