
class Calculator():
    def __init__(self, a, b):  #클래스가 만들어 질 때 작동
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    # def setData(self, a, b):
    #     self.a = a
    #     self.b = b

result = 0
while True:
    print('두 수를 입력해주세요')
    x, y = input().split()
    x = int(x)
    y = int(y)
    cal = Calculator(x,y)
    oper = ''

    print('1.더하기\n2.빼기\n3.곱하기\n4.나누기')  # 숫자 넣는 메뉴 구현하기
    choice = int(input())
    if choice == 1:
        result = cal.add()
        oper = '+'
    elif choice == 2:
        result = cal.sub()
        oper = '-'
    elif choice == 3:
        result = cal.mul()
        oper = '*'
    elif choice == 4:
        result = cal.div()
        oper = '/'
    else:
        break  # 그 외의 경우 종료
    print(cal.a, oper, cal.b, ' = ', result)

