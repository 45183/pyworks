# 5

# City 클래스 생성

class City:
    a = ["Seoul", "Incheon", "Daejeon", "Jeju", "Dokdo"]

# 전체 출력
# for c in City.a:
#     print(c)


# 첫글자만 출력
str1 = ' '      # 문자열을 담을 변수 선언

for c in City.a:
    # print(c[0])
    str1 += c[0]            # str1 = str1 + c[0]

print(str1)

