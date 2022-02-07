# 키보드로 거북이 조종하기

import turtle as t

def turn_right():
    t.setheading(0)             # 거북이의 머리 방향
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def clear():
    t.clear()


t.shape('turtle')
t.onkeypress(turn_right, "Right")       # 첫글자 대문자          # 함수 호출시 괄호 생략
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(clear, "Escape")
t.listen()                              # 실행 대기             # 필수, 넣지 않을 경우 작동x



t.mainloop()