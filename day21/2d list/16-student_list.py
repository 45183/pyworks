# 딕셔너리로 성적 통계 출력 : 학생 4명

student = [
            {"name":"이대한", "kor":80, "eng":80, "math":75},
            {"name":"박민국", "kor":70, "eng":65, "math":60},
            {"name":"오상식", "kor":75, "eng":70, "math":53},
            {"name":"최지능", "kor":95, "eng":90, "math":90}
    ]

# print("개수 :", len(student))

n = len(student)

# 개인별 총점과 평균
total = 0           # 개인별 총점

print(" 이름  총점 평균")
for std in student:
    total = std['kor'] + std['eng'] + std['math']
    avg = total / 3
    print("%s %d %.1f" % (std['name'], total, avg))
          # 문자 정수 실수


print()

# 과목별 총점과 평균
sum_subject = [0, 0, 0]
avg_subject = [0.0, 0.0, 0.0]


# 과목별 총점
for std in student:
    sum_subject[0] += std['kor']
    sum_subject[1] += std['eng']
    sum_subject[2] += std['math']



# 과목별 평균
avg_subject[0] = sum_subject[0] / n
avg_subject[1] = sum_subject[1] / n
avg_subject[2] = sum_subject[2] / n



# 과목별 총점 출력
print("국어 합계 : %d점" % sum_subject[0])
print("수학 합계 : %d점" % sum_subject[1])
print("영어 합계 : %d점" % sum_subject[2])


print()

# 과목별 평균 출력
print("국어 평균 : %.1f점" % avg_subject[0])
print("수학 평균 : %.2f점" % avg_subject[1])
print("영어 평균 : %.1f점" % avg_subject[2])

