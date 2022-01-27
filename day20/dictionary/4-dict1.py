# 딕셔너리 생성과 사용
# 딕셔너리 자료 구조 - 키와 값의 쌍으로 이루어짐


person = {}        # 빈 딕셔너리

print(person)


# 요소 추가
person['name'] = "오상식"
person['age'] = 40
person['phone'] = "010-1234-5678"


print()

# 특정 요소 조회 - key로 접근
print(person['name'])


print()


# 요소 삭제
del person['phone']


print()

# 요소 수정
person['name'] = "최지능"


# 전체 요소 조회
for key in person:
    print(key)                                  # key만 출력
    print(person[key])                   # 값(value) 출력
    print(key, ':', person[key])       # key : value



print()

# 객체 자료 출력
print(person)




