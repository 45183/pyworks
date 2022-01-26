# 1부터 10까지 출력

for i in range(1, 11):           
    print(i)

# range(초기값,  종료값, 증감값)        
                        # 실제 종료값 = 종료값 - 증감
                        # 증감값이 1일때 생략 가능

for i in range(1, 11):
    print(i, end=' ')              # 가로로 출력


for i in range(1, 11, 2):
    print(i)


for i in range(1, -11, -1):
    print(i)


print( )

for i in range(10):         # 초기값 생략하면 0부터 시
    print(i, end= ' ')

print( )

for i in range(1, 11):
    if i > 5:
        print(i, end=' ')           # 5보다 큰 수
        
print( )

for i in range(1, 11):          # 3의 배
    if i % 3 == 0:
        print(i, end=' ')
        
