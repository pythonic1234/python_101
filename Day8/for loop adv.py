#for_loop_adv
# for i in range(1000):
#     if i == 250:
#         print(i)
#         break

#for 문 컴프리헨젼
# 컴프리헨젼을 쓰면 보다 쉽게 데이터 정리가 가능함
# [표현식 for 미지수 in 리스트,문자열, range(n)]

# arr = [x*2 for x in range(100)]
# print(arr)
#
# #제곱수
# arr = [x for x in range(100) if x % (3*5) == 0]
# print(arr)
# #제곱
# arr = [x** for x in range(100) if x % (3*5) == 0]
# print(arr)


#0~100 사이에 짝수 and 5의 공배수이고 결과를 +10한 리스트

# arr1=  [i+10 for i in range(100) if i % (2*5) == 0]
# print(arr1)
#
# #위의 결과를 제외한 결과를 출력하려면 "=="를 "!="으로
# arr1=  [i+10 for i in range(100) if i % (2*5) != 0]
# print(arr1)

# lengths = [len(word) for word in ["hello", "world", "python"]]
# print(lengths)

# arr = [3,5,1,5,12,33,151]
# arr1 = [i*2 for i in arr]
# print(arr1)

# for a in range(1,10):
#     print(a % 2 == 0)




#arr1=  [i+10 for i in range(100) if i % (2*5) != 0]
# print(arr1)

#1. 자리 숫자의 합 구하기

# num = input("숫자 입력")
# sum = 0
# for i in num:
#     sum += int(i)
# print(sum)


#2. 배수만 골라내기
# num = int(input("제외할 배수 숫자 입력"))
# numlist1 = range(1,20)
# arr = [i for i in numlist1 if i % num ==0]
# print(arr)

#3. 대소문자 바꾸기

# word = input("영단어를 입력하세요")
# for i in word:
#     if (i.isupper()):
#         print(i.lower())
#     else:
#         print(i.upper())


#4. 특정 숫자의 자리 수 찾기

# num = input("숫자 아무거나 입력: ")
# find = input("찾고 싶은 숫자 입력: ")
# isFound = False
#
# for index,number in enumerate(num):
#     if(number == find):
#         print(index + 1)
#         isFound = True
#         break
#
# if isFound == False:
#     print(-1)