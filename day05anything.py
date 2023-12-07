# original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_list = [num for num in original_list if num % 2 == 0]
# print(even_list)
#
#
# nuber_list = [1,2,3,4,5,6,7,8,9,10]
# odd_list = [num for num in nuber_list if num % 2 !=0]
# print(odd_list)

# a = int(input("숫자를 입력하세요"))
# b = int(input("숫자를 입력하세요"))
#
# c = a + b
# print(f"두 숫자 합은: {c}입니다")


#뉴스 기사 단어 별로 정렬화 퀴즈

"Gold prices steady with US labor data, rate cut bets in focus"





#점심 메뉴 추천 프로그램

import random

# main_menu = ["짜장면", "짬뽕", "짬짜", "탕수육", "공복"]
# dessert_menu = ["아이스크림", "케이크", "과일", "벌레", "공복"]
# drink_menu = ["콜라", "사이다", "커피", "오렌지 주스", "아이스티"]
#
# random_main = random.choice(main_menu)
# random_dessert = random.choice(dessert_menu)
# random_drink = random.choice(drink_menu)
#
# print("메인은 이거 먹어라", random_main)
# print("후식은 이거 먹어라", random_dessert)
# print("음료는 이거 먹어라", random_drink)

# import random
#
# main = ["삼겹살", "돼지갈비", "갈매기살","껍데기"]
# drink = ["커피", "사이다", "콜라", "제로콜라"]
# dessert = ["사과","복숭아", "딸기", "포도"]
#
# random_main = random.choice(main)
# random_drink = random.choice(drink)
# random_dessert = random.choice(dessert)
#
# print(random_main,"이거드셈")
# print("이거드셈",random_dessert)
# print("이거드셈",random_drink)


# 10000초를 넣었을 때 몇분 몇시간인지 나타내기
#
# total_second = int(input("초를 입력하세요"))
# minute = total_second / 60
# hours = minute / 60
#
# print(f"입력한 {minute: .1f}초를 분으로 환산하면")
# print("입력한 초를 시간으로 환산하면", hours)
#






# 초를 넣었을 때 몇분 몇시간인지 나타내기
#
# num = int(input("양의 정수를 입력하세요:"))
# hour = num // 3600
# min = (num % 3600) // 60 #
# sec = num % 60
# print(f"{hour}시 : {min}분 : {sec}초")



# #뉴스기사
#
# article = " Gold prices moved little in Asian trade on Thursday as traders hunkered down in anticipation of more cues on a cooling U.S. labor market, while focus also remained on when the Federal Reserve planned to begin trimming interest rates."
# a = article.split()
# a.sort()
# print(a)


#점심 메뉴 추천 프로그램

# import random
#
# main = ["딸기,b,c,d,e"]
# drink = ["1,2,3,4,5"]
# dessert = ["q,w,e,r,z"]
#
# a = random.choice(main)
# b = random.choice(dessert)
# c = random.choice(drink)
#
# print(f"메인: {a}, 디저트: {b}, 음료: {c}")

#이거

# y = 20
# if y > 10:
#     print("y는 10보다 큽니다")
# if y > 15:
#     print("또한 y는 15보다 큽니다.")

# x = 0
# if x > 0:
#     print("x는 양수입니다")
# elif x == 0:
#     print("0 입니다")
# else:
#     print("음수 입니다")


# 100점이면 축하합니다 만점입니다
# 70점 이상이면 잘했다
# 70점 미만이면 열공하세요

# a = int(input("니 점수를 입력하세요"))
# if a >= 100:
#     print("축하합니다 만점입니다")
# elif 70 < a and a < 100:
#     print("잘했음")
# else:
#     print("열공하십쇼")

#양의 홀수? 양의 짝수? 음의 홀수? 음의 짝수 ? 0인지

# a = int(input("숫자를 입력해"))
# if a > 0:
#     if a % 2==0:
#         print("양의 짝수다")
# elif a > 0:
#     if a % 2==1:
#         print("양의 홀수다")
# elif a < 0:
#     if a % 3==0:
#         print("음의 홀수다")
# elif a < 0:
#     if a % 3==1:
#         print("음의 짝수다")
# elif a == 0:
#     print("0입니다")


#강사님 버전

# a = int(input("숫자"))
# if a > 0:
#     if a % 2 ==0:
#         print("양의 짝수")
#     else:
#         print("양의 홀수 입니다")
# elif a < 0:
#     if a % 2 == 0:
#         print("양의 짝수입니다")
#     else:
#         print("음의 홀수입니다")
#
# else:
#     print("0입니다")


# 문자 하나를 입력해서 알파벳이라면 알파벳입니다, 알파벳이 아니라면 알파벳이 아닙니다 프린트

# a = input("문자를 넣어주쇼")
# if a.isalpha():
#     print("알파벳이요")
# else:
#     print("알파벳이 아니요")

# 비밀번호 유효 타입 체크
# 유저한테 비밀번호 입력 받고
# 비밀번호의 시작이 영어 알파벳 대문자로 시작하면
# 비밀번호를 옳게 설정했수다
# 비밀번호 첫글자를 대문자로 설정하쇼

# password = input("원하는 비밀번호를 입력하쇼")
# if not(password[0].isupper()):
#     print("틀린 비밀번호, 비밀번호의 첫글자는 대문자로 설정해주세요")
#
# elif len(password) < 8:
#     print("비밀번호를 8자 이상 설정해주세요")
# elif password.isalpha():
#     print('비밀번호에 특수문자를 넣어주세요')
# else:
#     print("잘 설정하셨습니다")


#영어 점수, 등급 매기기

# score = int(input("당신의 점수를 입력해주세요"))
# if score == 100:
#     print("A등급 만점입니다")
# elif score >= 80:
#     print("B등급입니다")
# elif score >= 60:
#     print("C등급입니다")
# else:
#     print("D등급입니다")


#각도의 비밀을 밝혀라
# angle = int(input("각도를 입력해주세요"))
# if angle <= 90:
#     print("예각입니다")
# elif angle == 90:
#     print("직각입니다")
# elif 90 < angle and angle < 180:
#     print("둔각입니다")
# elif angle == 180:
#     print("평각입니다")

# 이거 다시 체크


# #대소문자 바꾸기
#
# word = input("문자를 입력해주세요")
# if word.isupper():
#     print(word.lower())
# else:
#     print(word.upper())


# 점수에 따른 등급과 피드백
#
# korean = int(input"한국어 점수를 입력해주세요")
# english = int(input"한국어 점수를 입력해주세요")
# math = int(input"수학점수를 입력해주세요")
#
# if korean == 100
#     print("good")
# elif english == 100
#     print("good")
# elif math == 100
#     print("good")
# else
#





#영화 티켓 예매 시스템


# a = int(input("니 점수를 입력하세요"))
# if a >= 100:
#     print("축하합니다 만점입니다")
# elif 70 < a and a < 100:
#     print("잘했음")
# else:
#     print("열공하십쇼")
