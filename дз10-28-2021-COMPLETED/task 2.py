import time
def TenToTwo(num):
    two=""
    while num>0:
        two=str(num%2)+two
        num=num//2
    return two
def TwoToTen(num):
    i=-1
    ten=0
    while num>0:
        ten=((num%10)*2**(i+1))+ten
        num=num//10
        i+=1
    return ten
print("Хотите ли вы что то посчитать?Если да то введите 'yes', если нет то 'no'")
answer0=input()
while answer0=="yes":
    print("если вы хотите перевести число из десятичной СС в двоичную,введите two")
    print("если вы хотите перевести число из двоичой в десятичную,введите ten")
    answer=input()
    if answer=="ten":
        print("введите число")
        num=int(input())
        print(TwoToTen(num))
    if answer=="two":
        print("введите число")
        num=int(input())
        print(TenToTwo(num))
    print("Хотите ли вы что то посчитать?Если да то введите 'yes', если нет то 'no'")
    answer0=input()
print("спасибо за использование программы")
time.sleep(5)