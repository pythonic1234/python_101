movie=int(input("영화의 종류?"))
age=int(input("나이는?"))
snack=int(input("스낵 패키지를 선택해주세요 (팝콘세트,스낵콤보,건강팩"))
seat=int(input("일반,프리미엄,vip중 좌석 타입을 골라주세요"))

if movie==1:
    cost=12000
elif movie==2:
    cost=10000
else:
    cost=11000

if age <18:
    cost*=0.8
elif age >65:
    cost *= 0.85
else:
    cost

if snack=="팝콘세트":
    cost += 6000
elif snack=="스낵콤보":
    cost += 8000
else :
    cost += 7000

if seat=="일반":
    cost += 0
elif seat=="프리미엄":
    cost += 5000
else :
    cost += 10000


print(f"금액은{cost}원 입니다")