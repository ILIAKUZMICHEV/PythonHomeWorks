s='Y'
while s=='Y':
    print("введите число 1")
    num1=float(input())
    print("введите операцию")
    op=input()
    print("введите число 2")
    num2=float(input())
    if op == "+":
        print(num1+num2)
    if op =="-":
        print(num1-num2)
    if op =="*":
        print(num1*num2)
    if op == "/":
        print(num1/num2)
    print("нажмиите Y,чтобы повторить или любую кнопку чтобы выйти.")
    s=input()
