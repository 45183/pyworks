# 1부터 n까지 곱하기(1x2x3x...xn)


def get_gob(n):
    gob = 1             # 곱하기는 1로 초기화
    for i in range(1, n+1):
        gob *= i
    return gob

print(get_gob(4))



def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n - 1)

'''
n = 4
4 * facto(3) = 4 * 3 * 2 * 1
4 * 3 * facto(2)
4 * 3 * 2 * facto(1)
'''

print(facto(4))