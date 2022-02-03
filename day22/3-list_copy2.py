# 리스트 내포

# [표현식 for 항목 in 리스트]

a = [1, 2, 3, 4, 5]
a2 = []
a3 = []
a4 = []
a5 = []

# 3의 배수로 저장

for i in a:
    a2.append(i * 3)

print("a2 = ", a2)


# 리스트 내포 구문
a3 = [i * 3 for i in a]

print("a3 = ", a3)


# 3의 배수이면서 짝수인 수
for i in a:
    if i % 2 == 0:
        a4.append(i * 3)

print("a4 = ", a4)


a5= [i * 3 for i in a if i % 2 == 0]
print("a5 = ", a5)

