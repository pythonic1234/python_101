movie=int(input("영화의 종류?"))
age=int(input("나이는?"))
if movie==1:
    cost=10000
elif movie==2:
    cost=8000
else:
    cost=9000

if age <13:
    cost*=0.5
elif 60<=age:
    cost *= 0.7
else:
    cost

print(f"금액은{cost}입니다")
