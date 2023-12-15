#리스트는 순서가 있고, 중복 가능
a=[1,2,3,4,5,1,2,3,4,5]

#셋은 순서가 없고, 중복 불가능
b={1,2,3,4,5,1,2,3,4,5} #1,2,3,4,5
print(b)

food={"쑥떡","피자","마라탕","떡볶이","마라탕"}
print(food)

d=set([1,2,3,4,5,1,2,3,4,5])
print(d)

#추가함수.add
food.add("붕어방")
food.add("라떼")
food.add("피자")
print(food)

#update 합집합
lunch={"라면","피자","파스타","샌드위치"}
dinner={"피자","샌드위치","없음","라떼"}
lunch.update(dinner)
print(lunch)

#제거 함수 remove or discard
dinner={"피자","샌드위치","없음","라떼"}
dinner.remove("없음")#없는 거 빼면 에러 남
print(dinner)
dinner.discard("라떼")#없는 거 빼도 에러 안 남
print(dinner)
#랜덤 제거 함수
dinner.pop()
print(dinner)

#모두 제거 함수 clear
dinner.clear()
print(dinner)

#세트의 수학적 연산
nation={"스위스","일본","태국","프랑스"}
europe={"스위스","프랑스","독일","영국"}

#합집합
uni=nation.union(europe)
print(uni)

#교집합
inter= nation.intersection(europe)
print(inter)

#차집합
diff=nation.difference(europe)
print(diff)

#대칭 차집합
symmetric=nation.symmetric_difference(europe)
print(symmetric)