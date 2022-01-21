print('введите первый список чисел')
set1={int(s) for s in input().split()}
print('введите второй список чисел')
set2={int(s) for s in input().split()}
print(len(set(set1&set2)))