# 기본 매개변수

# 매개변수를 초기화하여 선언하고 (count = 1),
# 함수 호출시 매개변수를 생략하면 기본값으로 출력된다.
def print_string(text, count=1):
    for i in range(count):
        print(text)


print_string("Hello")           # count 넣지 않을 경우 1
print('=' * 30)
print_string("Hello", 3)
