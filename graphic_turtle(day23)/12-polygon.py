import turtle as t

# 다각형 그리기

def polygon(n):
    for i in range(n):
        t.forward(50)
        t.left(360 / n)         # 다각형의 내각 공식

def polygon2(n, d):
    for i in range(n):
        t.forward(d)
        t.left(360 / n)

t.shape()           # 기본인경우(화살표) 생략가능

polygon(3)
polygon(5)

# 이동
t.penup()           # 펜 올리기 - 선 생기지 않음
t.forward(100)

t.color('blue')
t.pendown()         # 펜 내리기 - 다시 선 그려짐
polygon2(3, 100)
polygon2(5, 100)

t.mainloop()
