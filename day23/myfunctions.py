# 6

# 거듭제곱 함수 만들기

def mypow(x, y):
    num = 1
    for i in range(0, y):
        num *= x
        print("i =", i, ", num =", num)
    return num


# 절대값 함수

def myabs(x):
    if x < 0:
        return -x
    else:
        return x


if __name__=="__main__":            # 다른 곳에서 가져다 쓸때 출력 x
    print(mypow(2, 4))
    print(mypow(5, 3))
    print(myabs(-10))


# ctrl + d   -> vscode에서 alt + shift + 아래
