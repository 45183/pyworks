# 3

from day26.classlib.person import Person

class Employee(Person):                         # Person에 마우스 가져가면 import this name 선택해서 위의 from ~ import 자동완성 가능
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)             # 부모멤버 상속 키워드 - super()
        self.employee_id = employee_id

    def getid(self):
        return self.employee_id

emp1 = Employee("김산", 31, 1001)
print("이름 :", emp1.getname())
print("나이 :", emp1.getage())
print("사번 :", emp1.getid())