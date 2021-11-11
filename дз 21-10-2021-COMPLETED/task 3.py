list1 = [ int(s) for s in input().split() ]
print(list1)
list1.remove(max(list1))
print("2й максимум:",max(list1))