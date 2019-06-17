#  클래스 : 내가 직접 정의할 수 있는 자료형
#  계산기 설계도

#  클래스 안의 변수 : 필드
#  클래스 안에 만들어 놓은 함수 : 메소드

class Student:
    a = ''  # self.a랑 같음
    def __init__(self, a):  # 생성자
        self.a = a
    def printparam(self):
        print('클래스 변수(필드) = ' , self.a)


# a = Student()
myclass = Student('김영호')
myclass.printparam()
print(myclass.a)  # 해당 클래스의 필드 변수
b = Student('이영호')
print(b.a)