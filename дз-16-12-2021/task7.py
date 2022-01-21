synonyms = {}
num = int(input())
for i in range(num):
    first,second = input().split()
    synonyms[first]=second
    synonyms[second]=first
print(synonyms[input()])
