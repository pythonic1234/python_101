print(""
      "입장권 골라")
price = 0
parktiket =int(input("입장권의 종류?"))
age=int(input("나이는?"))
package=int(input("패키지 입력하세요?"))

ticket_dict = {
    1:50000,
    2:75000,
    3:100000,
}
package_dict={
    1:20000,
    2:15000,
    3:25000,
}

price = ticket_dict[ticket] + package_dict[package]

if age >=65:
    price *= 0.7
elif age <12:
    price *=0.5
else:
    price =price

print(f"총 금액은{price}원 입니다.")







# if parktiket==int("general"):
#     cost=50000
# elif parktiket==int("premium"):
#     cost=75000
# else: ()
#     cost=100000
#
# if age <12:
#     cost*=0.5
# elif 65<=age:
#     cost *= 0.3
# else:
#     cost
#
# if package == int("")
#
#
# print(f"당신의 금액은{cost}입니다")


