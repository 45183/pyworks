a = [100, 55, 65, 85, 90, 91, 85, 70, 60, 95]
sum = 0
avg = 0
idx = 0

for i in a:
    sum = sum + i

avg = sum / len(a)

print("합계 : " + str(sum))
print("평균 : " + str(avg))

print()

print("<등급 출력>")

for i in a:
    idx += 1
    if i >= 70:
        print(str(idx) + "번 학생은 1급입니다.")
    elif i >= 60 and i < 70:
        print(str(idx) + "번 학생은 2급입니다.")
    else:
        print(str(idx) + "번 학생은 불합격입니다.")


print()

a_idx = 0

for i in a:
    a_idx += 1
    if i >= 70:
        result = "1급"
    elif i >=60:
        result = "2급"
    else:
        result = "불합격"
    print(str(a_idx) + "번 학생은" + result + "입니다.")

print()

n = len(a)

for i in range(0, n):
    if a[i] >= 70:
        result = "1급"
    elif a[i] >= 60:
        result = "2급"
    else:
        result = "불합격"
    print("{}번 학생은 {}입니다.".format(i+1, result))