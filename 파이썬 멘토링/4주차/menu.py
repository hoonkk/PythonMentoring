from rpsGame import *  # 가위바위보 게임 불러오기
from calculator import *  # 계산기 불러오기
while True:
    print('Menu\n1.가위바위보 게임\n2.계산기')
    choice = int(input())
    if choice == 1:
        rpsgame()
    elif choice == 2:
        calculatorgame()
    else:
        print('종료합니다')
        break
