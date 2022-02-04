import turtle as t

t.setup(500, 500)           # 무대의 크기
t.bgcolor('black')          # 배경색
t.pensize(2)                # 선 두께 - 기본값 1
t.speed(0)                  # 속도 : 1 ~ 10 / 0이 가장 빠름
t.color('#0ff')             # 선 색

n = 50
for x in range(n):
    t.circle(80)
    t.left(360 / n)

t.mainloop()