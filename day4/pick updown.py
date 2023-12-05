# pick_updown
# 유저한테 해당 범위를 지정 받습니다. 1 ~ n
# n의 범위를 지정해주세요 !
# 1 ~ n 어떤 정수를 임의로 뽑고
# 총 5번 기회를 통해서 해당 숫자를 맞추기
# 숫자가 맞다면 맞습니다! 축하드립니다! 멘트 치기
# 틀리면 틀렸습니다. 다시 한번 맞춰보세요
import random

# import random
#
# answer = random.randint(1, 5)
# max_attempts = 2
#
# for attempt in range(max_attempts + 1):
#     user_input = int(input("1에서 5까지의 숫자 중 정답을 입력해보세요: "))
#
#     if user_input == answer:
#         print("정답입니다! 축하합니다.")
#         break
#     elif attempt < max_attempts:
#         print("틀렸습니다. 다시 시도하세요.")
#     else:
#         print(f"아쉽습니다. 정답은 {answer}입니다.")

# import random
#
# answer = random.randint(1,5)
# a = input("1에서 10까지의 숫자 중 정답을 입력해보세요")
# if a == answer:
#     print("정답입니다 축하합니다.")
# else:
#     print("틀렸습니다. 다시하세요")

# import random
#
# user = int(input("숫자의 범위를 지정하세요:"))
# pick = random.randint(1,user)
# target = int(input("해당 랜덤 숫자를 맞춰보세요!"))
# msg = "맞습니다! 축하드립니다" if pick == target else "틀렸습니다."
# print(msg)

player = ['손흥민', '김민재', '황희찬', '이강인']
a = random.randint(0,3)
b = random.choice(player)
random.shuffle(player)
c = random.uniform(1.5,2.5)

print(a)
print(b)
print(c)