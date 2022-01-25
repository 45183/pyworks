# 1부터 10까지 더하기

i = 1
sum_v = 0

"""
while i <= 10:
    sum_v += i
    print("i =", i, ", sum_v =", sum_v)
    i += 1              # i++ 사용불가
"""

'''
# while ~ break 문
while True:
    sum_v += i
    print("i =", i, ", sum_v =", sum_v)
    i += 1
    if i > 10:
        break               # if~break문 위치 위에 있어도 상관없음
'''

while True:
    if i > 10:
        break 
    sum_v += i
    print("i =", i, ", sum_v =", sum_v)
    i += 1


print("합계 :", sum_v)
