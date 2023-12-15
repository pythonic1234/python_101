# 1. for - range

# for i in  range(1000):
#     print(f"{i}비트코인은 지금 매도 타이밍")

# 2. for - list of str
# coin = ['비트코인', '이더리움', '리플', '에이다']
# for i in coin:
#     print(i)

# sign = "비트코인 떡상중 가즈아"
# for i in sign:
#     print(i)

#3. for i in enumerate(list or str)
# coin = ['비트코인', '이더리움', '리플', '에이다']
# for index, f in enumerate(coin):
#     print(index,f)

# arr = [3,1,23,5,13,45,15]
# total = 0
# for i in arr:
#     total = total +i
# print(f"위 배열의 평균은 {total/len(arr)} 입니다. ")

#1. 0~10000 사이의 정수를 뽑는 랜덤에서 n번 정수를 추출해서 평균값 계산하기

import random
n = int(input("몇번 돌려요 ?"))
arr = []
total = 0
for i in range(n):
    a = random.randint(0, 10000)
    arr.append(a)
    total=total+a
print(f"배열의 평균은{total/len(arr)}입니다")