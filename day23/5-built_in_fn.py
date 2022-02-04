# 내장 함수

# all() - 요소 중 0이 없으면 True
print(all([1, 5, 3]))
print(all([1, 0, 3]))

# any() - 모두 0 일때만 False
print(any([1, 2, 0]))
print(any([1, 0, 0]))
print(any([0, 0, 0]))

# round(n, digit) - (digit : 소수 몇번째까지, 없으면 정수로 반환)
print(round(4.6654, 2))
print(round(4.6654, 1))
print(round(4.6654, 0))
print(round(4.6654))

# eval(표현식) - 문자열을 숫자로 변환
x = 1
print(eval('x + 1'))

# list(str) - 문자열을 리스트로 변환
print(list("python"))

# sum(iterable) - 반복가능한 자료 더하기
print(sum([70, 80, 90]))

# min(iterable)
print(min([70, 80, 90]))

# pow() - 거듭제곱
print(pow(2,3))