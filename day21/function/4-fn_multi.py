# 두 수를 매개변수로 전달하여 서로 같으면 곱하고 다르면 더하는 함수를 정의하고 호출

'''
def data(x, y):
    if x == y:
        return x * y
    else:
        return x + y


n1 = data(5, 5)
n2 = data(5, 10)

print(n1)
print(n2)
'''


def data(x, y):
    if x == y:
        print(x * y)
    else:
        print(x + y)


n1 = data(5, 5)
n2 = data(5, 10)

