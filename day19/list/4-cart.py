# 리스트의 생성과 사용
cart = ['계란', '두부', '커피', '우유']
print('리스트의 크기 :', len(cart))
# len() : 리스트의 크기

print( )

# 특정 요소 조회
print(cart[2])

print( )

# 특정 요소 수정(변경)
cart[1] = '라면'

print( )

# 특정 요소 삭제
del cart[2]

print(len(cart))

print( )

# 특정 요소 추가  -  직접 추가 불가  -> append() 사
# cart[3] = '토마토'
cart.append("토마토")

print( )

# 전체 요소 조회  (for 변수 in 리스트) 
for i in cart:
#    print(i)
    print(i, end=' ')

print( )

# 전체 요소 조회 (for 변수 in range())
n = len(cart)
for i in range(0, n):
#for i in range(0, len(cart)):
#    print(cart[i])
    print(cart[i], end=' ')
