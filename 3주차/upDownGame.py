import random  # random 모듈 import
num = random.randint(1, 50)
while True:
    choice = int(input())
    if choice > num:
        print('Down')
    elif choice < num:
        print('Up')
    else:
        print('정답!')
        break

