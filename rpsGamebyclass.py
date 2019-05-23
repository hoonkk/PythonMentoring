import random


class Player:
    record = 0

    def __init__(self, name):
        self.name = name

    #  저번에 만든 걸 그대로 불러오기
    #  주의할 점 : self 추가해 줘야 함!
    def randomnum(self):
        rpsList = ['가위', '바위', '보']  # 가위, 바위, 보
        choice = random.choice(rpsList)  # Random으로 리스트 중 하나를 Choice해서 받아온다.
        return choice

    def checkwinner(self, user, computer):
        print('User : ', user, ', Computer : ', computer)
        if user == '바위':
            if computer == '바위':
                print('비겼습니다')
                return '무승부'
            elif computer == '가위':
                print('이겼습니다')
                return '승리'
            else:
                print('패배했습니다')
                return '패배'
        if user == '가위':
            if computer == '가위':
                print('비겼습니다')
                return '무승부'
            elif computer == '보':
                print('이겼습니다')
                return '승리'
            else:
                print('패배했습니다')
                return '패배'
        if user == '보':
            if computer == '보':
                print('비겼습니다')
                return '무승부'
            elif computer == '바위':
                print('이겼습니다')
                return '승리'
            else:
                print('패배했습니다')
                return '패배'

    def rpsgame(self):
        win = 0
        while True:
            computerChoice = self.randomnum()
            userChoice = self.randomnum()
            print('가위바위보 게임을 시작합니다. 엔터를 누르세요', end='')
            input()
            check = self.checkwinner(userChoice, computerChoice)
            if check == '승리':
                win += 1
            elif check == '패배':
                print(win, '번 이겼습니다\n')
                #  따로 추가해 줄 것
                self.record = win
                break


rankingList = []
while True:
    print('1. 게임 시작하기\n2. 기록 보기\n')
    menu = int(input())
    if menu == 1:
        print('사용자 이름을 입력하세요')
        playerName = input()
        player = Player(playerName)
        player.rpsgame()
        #  게임이 끝나면
        rankingList.append(player)
    elif menu == 2:
        for player in rankingList:
            print(player.name, '은 ', player.record, '승을 기록했습니다.', sep='')
