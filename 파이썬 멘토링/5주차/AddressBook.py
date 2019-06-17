class Person:
    def __init__(self, name, telnum):
        self.name = name
        self.telnum = telnum

    def printInformation(self):
        print('이름 : ', self.name, '\n전화번호 : ', self.telnum)

peopleList = []
while True:
    print('1.추가\n2.삭제\n3.검색\n4.전체 조회\n>>',end='')
    a = int(input())
    if a==1:
        print('이름을 입력하세요>>', end='')
        name = input()
        print('전화번호를 입력하세요>>', end='')
        telnum = input()
        a = Person(name, telnum)
        # 리스트에 추가하기
        peopleList.append(a)
    elif a==2:
        print('삭제할 회원의 이름을 입력하세요>>', end='')
        searchName = input()
        for person in peopleList:
            if(person.name==searchName):
                peopleList.remove(person)
    elif a==3:
        print('검색할 회원의 이름을 입력하세요>>' , end='')
        searchName = input()
        for person in peopleList:
            if(person.name == searchName):
                person.printInformation()
    elif a==4:
        for person in peopleList:
            person.printInformation()

