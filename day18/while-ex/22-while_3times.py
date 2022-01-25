# while문
# 책 146페이지 예제 2

result = 0
i = 1

while i <= 1000:
    if  i % 3 == 0:         # 3의 배수이면        # 등호 두개
        result += i         # 누적 합계
    i += 1

print(result)
