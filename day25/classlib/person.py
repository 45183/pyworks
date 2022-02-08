# 6

# 정보 은닉(Information Hide)
# 언더스코어가 1개 또는 2개가 있으면 멤버 접근 불가
class Person:
    def __init__(self):
        self._name = ""         # __ 2개도 가능
        self._age = 0
        
p1 = Person()
# p1.   - 멤버 변수에 접근 불가 (self._name)