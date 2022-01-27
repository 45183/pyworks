# set() 메서드(함수) 사용


# 집합 생성
s = {1, 2, 3}


# 요소 추가 - add()
s.add(4)

print(s)


# 요소 삭제 - remove()
s.remove(3)

print(s)


# 전체 삭제 - clear()  - 빈 집합 : set()
s.clear()

print(s)



# in 집합
fruit = {"사과", "바나나", "포도", "사과"}

print("바나나" in fruit)
print("포도" not in fruit)


for i in fruit:
    print(i, end = " ")         # 순서 없음, 중복 불허

# 집합 객체 출력
print(fruit)
