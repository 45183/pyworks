# 구구단 출력
'''
dan = 7

for i in range(1, 10):
    print(dan, 'x', i, '=', dan * i)
'''

# 단을 입력받아서
'''
x = input("단을 입력해주세요 : ")
dan = int(x)

# dan = int(input("단을 입력해주세요 : "))

for i in range(1, 10):
    print(dan, 'x', i, '=', dan * i)


print("단을 입력해주세요")
dan = int(input())                  # 아래
for i in range(1, 10):
    print(dan, 'x', i, '=', dan * i)
'''


dan = int(input("단을 입력해주세요 : "))

for i in range(1, 10):
#    print(dan, 'x', i, '=', dan * i)
    print("{} x {} = {}".format(dan, i, dan * i))
