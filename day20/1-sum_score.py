# score list 생성과 저장
score = [70, 80, 20, 90,100, 50]


# 합계
sum_v = 0


'''
# fon in list 문
for i in score:
    sum_v += i

print("합계 :", sum_v)
'''

# for in range()문
for i in range(0, len(score)):
    sum_v += score[i]

print("합계 :", sum_v)


# 평균 계산
avg = sum_v / len(score)

print("평균 :", avg)

print("평균 : %.2f" % avg)            # %.2f - 소수 둘째자리까지
# %d - 정수 대응문자
# %f - 실수 대응문자



# 내장 함수 - sum()
print("합계 :", sum([70, 80, 20, 90,100, 50]))
print("합계 :", sum(score))
