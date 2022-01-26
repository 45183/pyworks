# 문자열 처리 함수 - split()
# 문자열을 리스트로 반환함

f = "사과, 딸기, 포도"
f = f.split(',')                # 구분기호
print(f)
print(f[0])

'''
a = "사과 딸기 포도"
a = a.split()                # 구분기호 - 공백문자 (' ') 도 가능
print(a)
print(a[0])
print(a[1:])
'''


# 구분기호(콜론)

s = "a:b:c:d"
s = s.split(":")
print(s)



# replace('변경전 문자열', '변경후 문자열')
s2 = "Hello, world"
s2 = s2.replace('world', 'korea')
print(s2)


