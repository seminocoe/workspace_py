"""
10진수를 2진수로 변환
1은 빨간색 거북이 크기는 2배
0은 파란색 거북이로 표시하여 출력
"""

import turtle
#전역변수 선언
num = 0
swidth, sheight = 1000, 300

curX, curY = 0, 0

#실행 부 작성
if __name__ == "__main__":
    turtle.title("거북이로 2진수 표현하기")
    turtle.shape("turtle")
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num=(int)(input("숫자를 입력하세요:"))
    binary = bin(num)
    curX = swidth / 2
    curY = 0

    for i in range(len(binary)-2) :
        turtle.goto(curX,curY)
        print(num)
        print(num & 1)
        if num & 1 :#숫자를 2진수로 변환했을 때 비트가 1인지를 체크함
            turtle.color('red')
            turtle.turtlesize(2)
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX-=50
        num >>= 1

turtle.done()