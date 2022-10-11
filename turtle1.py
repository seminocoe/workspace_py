import turtle as t
import random

score = 0
playing = False

ts = t.Turtle()
ts.shape("turtle")
ts.color("red")
ts.speed(9)    # 악당 거북이의 속도를 9로 설정합니다    
ts.up()
ts.goto(0,200)

te = t.Turtle() 
te.shape("circle")
te.color("green")
te.speed(9)
te.up()
te.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def start():
    global playing    # playing 변수를 play()함수 밖에서도 사용할 수 있도록 global 지정해줌
    if playing == False:    # 게임이 대기중(False)인 상태이면 
        playing == True
        t.clear()    # 화면상의 메시지를 지웁니다
        play()    # t.play() -> 오류가 발생하여 play()로 수정 (2019.10.18)

def play():
    global score
    global playing
    t.forward(10)

    if random.randint(1,5) == 3:    # 악당 거북이가 항상 주인공을 따라오는 것이 아니라 20%의 확률로 따라옴
        ang = ts.towards(t.pos())     
        ts.setheading(ang)
    speed = score + 5   # 점수에 5를 더해서 속도를 올립니다. (점수가 높아질 수록 빨라짐)

    if speed > 15:
        speed = 15    # speed가 15를 넘지는 않도록 설정합니다.
    ts.forward(speed)

    if t.distance(ts) < 12:    # 주인공과 악당 사이의 거리가 12보다 작으면 게임을 종료합니다
        text =  "Score: " + str(score)
        message("Game Over",text)
        playing = False    # 게임을 종료할 수 있도록 playing = False 설정
        score = 0

    if t.distance(te) < 12:     # 주인공과 먹이 사이의 거리가 12보다 작으면 
        score = score + 1
        t.write(score)      # 점수를 화면에 표시합니다
        star_x = random.randint(-230,230)    
        star_y = random.randint(-230,230)
        te.goto(star_x,star_y)    # 먹이를 임의생성된 위치로 보냅니다

    ''' score = 5일 때 악당 거북이 한 마리를 추가합니다 ''' 
    if score == 5:
        ts2 = t.Turtle()
        ts2.shape("turtle")
        ts2.color("blue")
        ts2.speed(9)    # 악당 거북이의 속도를 9로 설정합니다    
        ts2.down()
        ts2.goto(0,100)

    if playing:     # if playing == True 와 같은 의미. 게임을 계속 이어갈 수 있게 해주는 중요한 if절
        t.ontimer(play,100)    # 게임 플레이 중이면 0.1초 후 play함수를 실행합니다.
        
def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",20))
    t.goto(0,-100)
    t.write(m2,False,"center",("",15))
    t.home()

t.title("Turtle Run")
t.setup(50,50)    # 창의 크기를 50 x 50 으로 설정 (?)
t.bgcolor("black")
t.shape("turtle")
t.speed(9)
t.up()
t.color("white")

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")    # space키는 소문자!
t.listen()

message("Turtle Run","[Space]")
