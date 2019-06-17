import random


def randomnum():
    rpsList = ['가위', '바위', '보']  #  가위, 바위, 보
    choice = random.choice(rpsList)  #  Random으로 리스트 중 하나를 Choice해서 받아온다.
    return choice


def checkwinner(user, computer):
    print('User : ', user, ', Computer : ', computer)
    if user== '바위':
        if computer == '바위':
            print('비겼습니다')
            return '무승부'
        elif computer == '가위':
            print('이겼습니다')
            return '승리'
        else:
            print('패배했습니다')
            return '패배'
    if user== '가위':
        if computer == '가위':
            print('비겼습니다')
            return '무승부'
        elif computer == '보':
            print('이겼습니다')
            return '승리'
        else:
            print('패배했습니다')
            return '패배'
    if user== '보':
        if computer == '보':
            print('비겼습니다')
            return '무승부'
        elif computer == '바위':
            print('이겼습니다')
            return '승리'
        else:
            print('패배했습니다')
            return '패배'

def rpsgame():
    win = 0
    while True:
        computerChoice = randomnum()
        userChoice = randomnum()
        print('가위바위보 게임을 시작합니다. 엔터를 누르세요', end='')
        input()
        check = checkwinner(userChoice, computerChoice)
        if check == '승리':
            win += 1
        elif check == '패배':
            print(win, '번 이겼습니다\n')
            break

