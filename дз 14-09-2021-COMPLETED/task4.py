n=int(input())
list1=[0,1]
for i in range(0,n):
    list1[i]=list1[i-1]+list1[i-2]
    list1.append(list1[i])
print(list1[n])
    

    
    