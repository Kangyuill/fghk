# 주제: 함수

# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값


## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle
<DrawStar_100 함수 정의>

win = turtle.Screen()
<DrawStart_100 함소 호출>
win.mainloop()
'''

## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
<DrawStar() 함수 정의해주기> 

win = turtle.Screen()
DrawStar(200)
win.mainloop()
'''

## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
<getRandomNum() 함수 정의해주기>

<getRandomNum() 함수를 호출하여 반환값을 num 변수에 할당하기>
print(num)
'''

## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
<add() 함수 정의해주기>

<add() 함수를 호출하여 반환값을 X 에 할당하기 >
print(X)
'''

## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 30p - 함수 Mission 참고
'''
# Mission: draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    """
    # 설정(작성할 부분1)
    ## 여기에 rainbow_color 리스트 작성해주세요
    t.pensize(pen_size)

    # 그리기
    t.setheading(90)
    t.penup()
    t.setpos(x+(rainbow_size / 2 - i * pen_size), y)
    t.pencolor(#작성해주세요#)
    t.pendown()
    t.speed(10)
    t.circle((rainbow_size / 2 - i * pen_size), 180)


import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

# 이제 draw_rainbow 함수를 활용하여 무지개를 마음껏 그려보자(작성할 부분3)


turtle.mainloop()
'''

##
'''
a = ['바나나','딸기','포도','사과','멜론','복숭아']

#print(a[0],a[1],a[2])

for f in range(1,4):
    print(a[f])


for i in range(1,100,2):
    print(i)

year = int(input('년도를 입력하세요: '))

if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
    print(1)

a = 0
while a < 100:
    a += 1
    print(a)

a = 0
while a < 3:
    a += 1
    print(f"{a}꼬마")
print("인디언!")
'''

while True:
    p = int(input("숫자를 입력하세요: "))
    if p == 1:
        print("끝!")
        break

'''
a = 0
while a < 100:
    a += 1
'''



