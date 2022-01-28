# 1 ~ 100까지 자연수 중 4의 배수와 개수를 출력하는 프로그램

def get_times(n):
    for i in range(1, 101):
        if i % n == 0:
            global count
            count = count + 1
            print(i, end=" ")

count = 0               # 배수의 개수
get_times(4)
print("\n배수의 개수 :", count)          # \n - 줄바꿈
