# 주제: 딕셔너리

## [딕셔너리]
## : 키(key)와 데이터(value)를 가지고 있는 "사전과 같은 자료형"
## key값을 통해 value값을 불러올 수 있다.

## 연습문제1: 딕셔너리 만들기
## : 자신이 좋아하는 youtuber 채널이름(key)과 구독자 수(value)를 말해보자.
##   그리고, 모두가 말한 youtuber들의 이름과 구독자수로 dictionary 자료형을 만들어보자.
##   만약, 남은 시간이 얼마 없다면, 미리 작성해놓은 데이터를 사용하도록 하자

youtuber = {
    "PAKA" :1500000,
    "oyo" : 120000,
}

# dic = {
#     "사과" : "apple",
#     "포도" : "grape",
# ## 연습문제2: 딕셔너리 제어1-값에 접근하기
# ## : 자신이 가장 좋아하는 youtuber의 구독자 수를 출력해보자
#
# print(youtuber["PAKA"])     # ()안에 값에 접근하는 문장 넣어주기
# print(dic["사과"])
#
# a = input("과일을 입력하세요")
# print(f"{a}는 영어로 "dic[a],"입니다")
#
# ## 연습문제3: 딕셔너리 제어2-값 할당(or 수정)하기
# ## : 자신이 가장 좋아하는 유투버의 구독자 수에 1000이 더 큰 숫자를 넣고 이를 출력해보자
#
# del youtuber["우주하마"]                         # 딕셔너리 값 할당 명령 수행
# print(youtuber)
#
# youtuber["PAKA"] = 2000000
# print(youtuber)



## 연습문제3: 딕셔너리 제어3-삭제하기
## : 자신이 두번째로 좋아하는 youtuber를 딕셔너리에서 삭제해보자
'''
                              # 딕셔너리 값 지우기 명령 수행
print(youtuber)
'''
## 연습문제4: 딕셔너리 관련 함수
## .items(), .keys(), .values()의 결과와 데이터 타입을 출력해보자
## ※ 결과 확인이 중요!!

print(youtuber.items())     # .items(): key와 value 쌍을 반환하는 함수
print(youtuber.keys())     # .keys(): 원소가 key로 이루어진 데이터를 포함하는 list를 반환하는 함수
print(youtuber.values())     # .values(): 원소가 value로 이루어진 데이터를 포함하는 list를 반환하는 함수
