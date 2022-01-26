'''
# 1부터 10까지의 합계

sum_v = 0

for i in range(1, 11):
    sum_v += i
    print('i =', i, 'sum_v =', sum_v)

print("합계 :", sum_v)


# 1부터 10까지 곱

facto = 1

for i in range(1, 11):
    facto *= i
    print('i =', i, 'facto =', facto)

print("결과 :", facto)
'''

# 1부터 n까지의 합계 (n은 입력값)

n = int(input("숫자를 입력해주세요 : "))
'''
n = input("숫자를 입력해주세요 : ")
n = int(n)                                        
'''
sum_v = 0

for i in range(1, n + 1):
    sum_v += i
    print('i =', i, 'sum_v =', sum_v)


print("합계 :", sum_v)
