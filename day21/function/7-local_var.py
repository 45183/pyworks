# 지역변수(local variable)의 유효범위(scope)

def one_up():
    x = 1
    x = x + 1
    return x

print(one_up())     # 2
print(one_up())     # 2
# print(x)              #  not defined
