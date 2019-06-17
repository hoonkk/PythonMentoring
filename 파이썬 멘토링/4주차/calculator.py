from operation import *

def calculatorgame():
    result = 0
    while True:
        print('두 수를 입력해주세요')
        x , y = input().split()
        x = int(x)
        y = int(y)
        oper = ''

        print('1.더하기\n2.빼기\n3.곱하기\n4.나누기')
        choice = int(input())
        if choice == 1:
            result = add(x, y)
            oper = '+'
        elif choice == 2:
            res= subult (x, y)
            oper = '-'
        elif choice == 3:
            result = mul(x, y)
            oper = '*'
        elif choice == 4:
            result = div(x ,y)
            oper = '/'
        else:
            break  # 그 외의 경우 종료
        print(x , oper , y , ' = ', result)
