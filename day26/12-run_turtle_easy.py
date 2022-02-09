import turtle as t
import random

def turn_right():
    t.setheading(0)
def turn_up():
    t.setheading(90)
def turn_left():
    t.setheading(180)
def turn_down():
    t.setheading(270)

def play():
    t.forward(10)                   # 주인공 거북이 10px 이동
    te.forward(9)                   # 적 거북이 9px 이동
    angle = te.towards(t.pos())     # 적 거북이가 주인공 거북이 쫓아감
    te.setheading(angle)            # 적 거북이의 머리 방향을 주인공 거북이 방향으로 설정

    # 거북이 사이의 거리가 멀때만 게임이 작동
    if t.distance(te) >= 12:
        t.ontimer(play, 100)  # 0.1초 간격으로 play 콜백

    # 먹이에 닿으면 새로운 위치로 이동
    if t.distance(tf) < 12:
        x = random.randint(-230, 230)        # 가로의 길이가 500이므로
        y = random.randint(-230, 230)
        tf.goto(x, y)


# 주인공 거북이
t.shape('turtle')
t.setup(500, 500)
t.bgcolor('white')
t.color('black')
t.speed(0)
t.up()

# 적 거북이
te = t.Turtle()
te.shape('turtle')
te.color('red')
te.up()
te.speed(0)
te.goto(0, 200)

# 먹이
tf = t.Turtle()
tf.shape('circle')
tf.color('green')
tf.speed(0)
tf.up()
tf.goto(0, -200)


# 키 작동
t.onkeypress(turn_right, 'Right')
t.onkeypress(turn_up, 'Up')
t.onkeypress(turn_left, 'Left')
t.onkeypress(turn_down, 'Down')
t.listen()
play()


t.mainloop()
