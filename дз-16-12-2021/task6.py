set1 = {}
for word in input().split():
    set1[word] = set1.get(word, 0) + 1
print(set1)