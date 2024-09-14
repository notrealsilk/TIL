#3장

#연산자
print(1+1)#덧셈
print(1-1)#뻴셈
print(5*2)#곱셈
print(6/3)#나눗셈

print(2**3) #제곱 2^3=8
print(5%3) #나머지 : 2
print(5//3) #몫 : 2

print(10>3) #True
print(4>=7) #False
print(10<3) #False
print(5<=5) #True

print(5==5) #True
print(3==4) #False
print(3+4==7)#True

print(1!=3)#True (!= : not과 같음)
print(not(1!=3)) #False

#and (모두 만족해야 True)
print((3>0) and (3<5)) #True : (and=&)
print((3>0) & (3<5)) #True

#or (하나만 만족해도 True)
print((3>0)or(3>5)) #True : (or=|)
print((3>0)or(3>5)) #True

print(5>4>3) #True
print(5>4>7) #False

#간단한 수식

print(2+3*4)#14
print((2+3)*4) #20

number = 2+3*4 #14

print(number) 
number = number + 2 #16

print(number) #16
number += 2 #18 (number 더하기 2 = 18)
print(number) #18
number /= 2 #9 (number 나누기 2)
print(number) #9
number *= 2 #18 (number 곱하기 2)
print(number) #18
number -= 2 #16 (number 빼기 2)
print(number) #16

number %=2 #% : 나머지
print(number) #0

#숫자 처리 함수

print(abs(-5)) #abs() : abs 값 안의 절댓값 #5
print(pow(4,2))#Pow(숫자1, 숫자2) : 숫자1의 숫자2 승 #4^2=4*4=16
print(max(5,12)) #max() : 최댓값 산출 #12
print(min(5,12)) #min() : 최솟값 산출 #5
print(round(3.14)) #round() : 반올림 #3


from math import * #math 라이브어리 안에 있는 모든 것을 이용하겠다.
print(floor(4.99)) #내림 #4
print(ceil(3.14)) #올림 #4
print(sqrt(16)) #제곱근 #4

#랜덤 함수

from random import * #랜덤 함수=random 모듈 불러오기

print(random()) #난수가 랜덤 / 0.0이상, 1.0 미만의 임의 값을 생성
print(random()* 10) #0.0~10.0 미만의 임의 값을 생성

print(int(random()*10))#int() :  소수점 자리 안 나오게, 즉 정수로 보여줌 #0~10 미만의 임의 값을 생성
print(int((random()*10))+1) #1~10 이하의 임의의 값

print(int(random()*45)+1) #1~45 사이의 임의의 값 생성

print(randrange(1,45)) #1~45 미만의 임의의 값 생성

print(randint(1,45)) #1~45 이하의 임의 값 생성

#3강 퀴즈
"""월 4회 스터디, 3번은 온라인, 1번은 오프라인

조건1 : 랜덤 날짜
조건2 : 최소 일수인 28 이내로 정함
조건 3 : 매월 1~3일은 제외

(출력문 예제) : 오프라인 스터디 모임 날짜는 매웥 x일로 선정되었습니다."""

from random import *

day=randint(4,28)

print('오프라인 스터디 모임 날짜는 매월' +str(day)+'일로 선정되었습니다.') #str() : 정수형-> 문자형으로

