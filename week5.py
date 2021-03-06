# 주제: 리스트 자료형

# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]

## 연습문제>> 내가 자주보는 유투버 이름 각자 1개씩 카톡방(혹은 채팅방)에 올리고
## 이 이름들을 list로 만들기

'''
youtuber = ["핫소스","파카","faker","최케빈"]
youtuber[3] ="ㅇ"
print(youtuber)

del youtuber[0]
print(youtuber)
'''

'''
youtuber = ["핫소스","파카","faker","최케빈"]
print(youtuber[1:3])
print(youtuber[-1]) 
print(youtuber[:])
print(len(youtuber))
'''

'''
a = ['다','바','가','나','이']
print(sorted(a,  reverse = True))
'''

'''
number = [1,2,3,4,5,6,7]
print(number)
print(type(number))
'''

'''
fruit = ["사과","바나나"]
what = input("좋아하는 과일 입력: ")
if what == "포도" or what == "메론" or what == "참외" or what == "수박" or what == "딸기" :
    fruit.append(what)
else:
    print("과일이 아닙니다.")
print(fruit)
'''

'''
youtuber = []
print(youtuber)
'''








## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.


'''
<명령입력>
'''
'''
print(youtuber)
'''


'''
fruit = ["사과","바나나"]
what = input("좋아하는 과일 입력: ")
if what == "포도" or what == "메론" or what == "참외" or what == "수박" or what == "딸기" :
    fruit.append(what)
else:
    print("과일이 아닙니다.")
print(fruit)

## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자
print(<명령입력>)






## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자
<명령입력>
print(youtuber)

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.
<명령입력>
print(youtuber)

## 리스트 제어하기5: 리스트 슬라이싱
## 방법: 리스트이름[처음:끝+1]
## 연습문제>> 처음~3번쨰, 2번째~끝, 3번째~4번째에 위치한 유투버들만, 그리고(':'를 활용하여) 리스트 전체을 출력해보자.
print(youtuber[:5])

## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## 연습문제>> 현재 리스트에 포함된 데이터의 개수를 구해보자
print(<명령입력>)

## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## 연습문제>> 유투버들을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자
<명령입력>
print(youtuber)
<명령입력>
print(youtuber)
'''

## 리스트 mission1
## :RGB 색상(red, green,blue)을 리스트에 저장하고
##  turtle 모듈을 활용하여 색상이 서로 다른 직선을 그려보자
##  (설정: 굵기(30), 선 길이(200))

import turtle

# 작성1: 리스트 color 선언하기

'''
color = ['red','green','blue']
win = turtle.Screen()
win.setup(600,600)
t = turtle.Turtle('turtle')
t.pensize(30)

t.penup()
t.pencolor(color[2])
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, 100)
t.pencolor(color[1])
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, 50)
t.pencolor(color[0])
t.pendown()
t.fd(200)

win.mainloop()
'''

'''
## 리스트 mission2
## 다음은 1번~5번 학생의 1분간 턱걸이 개수이다

pull_up = [3, 16, 2, 5, 10, 7]
## 1번 문제: 7번째 학생의 턱걸이 개수가 9라고 할 때, 이를 리스트에 추가해보자
pull_up.append(9)
print(pull_up)
## 2번 문제: 2번 학생의 재측정 결과 20개의 턱걸이를 하였다. 리스트에 데이터를 수정해보자
pull_up[1] = 20
print(pull_up)
## 3번 문제: 3~7번까지의 학생의 턱걸이 갯수만을 뽑아 temp 변수에 저장하고 출력해보자
temp = pull_up[2:8]
print(temp)
## 4번 문제: 학생들의 턱걸이 횟수 데이터를 오름차순으로 정렬
pull_up = sorted(pull_up)
print(pull_up)
'''

##리스트 추가 미션1


'''
menu = ["햄버거","치킨","피자"]
a = int(input("주문할 메뉴를 말하세요: "))
if a== "햄버거" :
    print(5000)
'''

##리스트 추가 미션2








'''
x=10
y=20
z=x
x=y
y=z
print(x,y)
'''

'''
cham = int(input("참석자의 수을 입력하세요: "))
print(1*cham)
print(2*cham)
print(4*cham)
'''


a = int(input("시작의 숫자를 입력하세요.: "))
b = int(input("끝나는 숫자를 입력하세요.: "))
sum = 0
for x in range (a,b+1):
    if x % 2 != 0 :
        sum = sum + x
print(sum)












