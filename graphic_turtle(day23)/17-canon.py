# 거북이 대포 게임

import turtle as t
import random as r

t.shape()


def turn_up():
    t.left(2)


def turn_down():
    t.right(2)


def fire():
    angle = t.heading()         # 거북이가 바라보는 각도
    while t.ycor() > 0:         # 거북이가 땅 위에 있는 동안 반복(turtle이 y좌표 0 보다 클때)
        t.forward(15)           # 15픽셀 직진
        t.right(5)              # 각도 5도씩 줄어든다.

    d = t.distance(target, 0)   # 거북이와 목표 지점과의 좌표 저장
    t.sety(r.randint(10, 100))  # y 좌표의 위치 (성공 또는 실패 문자 표시)

    if d < 25:                  # 명중한 것으로 간주
        t.color('blue')
        t.write('Good!', False, 'center', ('', 15))         # 출력함수 (문자열, bool, 정렬, 글꼴)
    else:                        # 명중하지 못한 경우 처음 위치로 돌아가서 반복
        t.color('red')
        t.write('Bad!', False, 'center', ('', 15))
        t.color('black')
        t.goto(-200, 10)        # 발사위치로 돌아감
        t.setheading(angle)     # 저장된 각도로 돌아감 (하지 않는 경우, 발사 이후 떨어질때 각도)

# 땅 그리기
t.goto(-300, 0)
t.goto(300, 0)

# 목표 지점
target = r.randint(50, 150)
t. pensize(2)
t.color('green')
t.up()
t.goto(target-25, 2)
t.down()
t.goto(target+25, 2)

# 발사 위치
t.color('black')
t.up()
t.goto(-200, 10)
t.setheading(20)




# 대포 동작
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")     # 스페이스바는 소문자로만 사용
t.listen()

t.mainloop()