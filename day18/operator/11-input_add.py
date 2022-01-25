# 두 수를 입력받아서 계산하기
"""
x = input("첫째 수 입력 : ")
y = input("둘째 수 입력 : ")

add = x + y
print(add)
# 문자열 합
"""

'''
x = int(input("첫째 수 입력 : "))
y = int(input("둘째 수 입력 : "))

add = x + y
print("두 수의 합 :", add,"입니다.")
#print("두 수의 합 : " + add)        # 에러 (문자 + 숫자)
print("두 수의 합 : " + str(add) + "입니다.")
# '+'로 문자열 연결할때, 숫자형은 다시 문자형으로 변환해야함
'''


x = input("첫째 수 입력 : ")
y = input("둘째 수 입력 : ")

add = int(x) + int(y)
print("두 수의 합 :", add,"입니다.")
print("두 수의 합 : " + str(add) + "입니다.")
