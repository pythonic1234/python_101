#만나이 계사

# # 연도 = float(input("태어난 연도를 입력해주세요"))
# # 만나이 = float(int("2023") -int(연도))
# # print(f"당신의 만나이는 {만나이}입니다")

# 태어난연도 = int(input("태어난 연도 입력"))
# 현재연도 = 2023
# 만나이 = 현재연도 - 태어난연도
# print(f"당신의 만 나이는 {만나이} 입니다")

#세개 숫자 합의 평균

# 숫자1 = int(input("숫자a를 입력해주세요"))
# 숫자2 = int(input("숫자b를 입력해주세요"))
# 숫자3 = int(input("숫자c를 입력해주세요"))
#
# average = (숫자1+숫자2+숫자3 / 3)
# print(f"평균은 {average}입니다:")
#
# #환율 계산
#
# 엔화 = float(input("엔화의 환율을 입력해주세요"))
# 달러 = float(input("달러의 환율을 입력해주세요"))
#
# 원화환전금액 = float(input("원하는 원화 환전금액 krw"))
#
# 원달러환율 = 원화환전금액 / 달러
# 원엔환율 = 원화환전금액  / 엔화
#
# print(f"달러로 환산하면{원달러환율}입니다")
# print(f"엔화로 환산하면{원엔환율}입니다")
#
# won = int(input("원화 입력"))
# print(f"엔화로는 {won/8.8} 달러로는 {won/1280}입니다. ")
#

#거리 변환
#
# km =float(input("거리 입력"))
# print(f"마일로 환산하면 {km *0.62}입니다")

# #섭씨 -> 화씨 변환
# c = float(input("섭씨를 입력해주세요"))
# print(f"{c*9/5+32} 화씨 입니다")


#반지름을 입력 받을 때 원의 둘레를 출력하는 프로그램

# 반지름 = float(input("반지름을 입력하세요"))
# 원둘레 = 2 * 3.14 * 반지름
# print(f"원의 둘레는 {원둘레}입니다")
#
# #반지름을 입력 받을 때 원의 넓이를 출력하는 프로그램
# 반지름 = float(input("반지름을 입력하세요"))
# 원넓이 = (반지름)*(반지름)*3.14
# print(f"원의 넓이는 {원넓이}")

#반지름을 입력 받을 때 원의 부피를 출력하는 프로그램

반지름 = float(input("반지름을 입력하세요"))
부피 = 4/3 * 3.14 * 반지름 * 반지름 * 반지름
print(f"원의 부피는 {부피:2f}입니다.")

#한 변의 길이를 입력하고 정사각형의 둘레와 넓이를 출력하는 프로그램
side = int(input("한변 길이 ㄱ"))
print(f"둘레 {side * 4} 넓이 {side * side}")