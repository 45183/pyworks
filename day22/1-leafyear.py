# 윤년을 판별하는 프로그램

# 조건 :4년마다(4의 배수), 100년 단위는 아니나, 400년 단위는 윤년이다.

year = int(input("연도를 입력해주세요 : "))

if year % 400 == 0:
    print("윤년입니다.")
elif year % 100 == 0:
    print("평년입니다.")
elif year % 4 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")


'''
if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
    print("윤년입니다.")
else:
    print("평년입니다.")
'''