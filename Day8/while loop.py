import random

a = 0
while True:
    print("""
    1. 랜덤 번호 6개 출력
    2. 시스템 종료
    """)
    a = int(input("번호 입력:"))
    if a ==1:
        for i in range(6):
            print(random.randint(0,45))
    elif a == 2:
        break
    else :
        print("숫자를 잘못 입력하셨습니다.")