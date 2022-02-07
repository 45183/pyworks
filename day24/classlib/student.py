# 2
# Student 클래스 정의와 사용

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):          # 객체의 정보 출력
        return "이름 : {}, 학년 : {}".format(self.name, self.grade)

    def learn(self):
        return "수업을 듣습니다."

'''
s1 = Student('콩쥐', 1)
print("이름 :", s1.name)
print("학년 :", s1.grade)

s2 = Student('팥쥐', 2)
print("이름 :", s2.name)
print("학년 :", s2.grade)
'''


'''
객체지향언어의 특성
1. 캡슐화(추상화) - 멤버변수, 메서드(함수) 포함
2. 정보은닉 
- get(), set() 함수
- 멤버 변수 : private(접근 불가)으로 만듦 / (public - 접근가능)
3. 상속과 다형성
'''

if __name__=="--main--":
    s1 = Student('콩쥐', 1)
    s2 = Student('팥쥐', 2)
    print(s1)
    print(s2)