#조건문_if문
#조건이 참이면 실행문을 실행하는 조건문 / 조건이 거짓이면 실행문은 건너뛴다

x = 10
if x > 5 :
    print('x는 5보다 크다') #이 조건이 참이면
    print('그래서, 조건문은 참이다') # 이 코드들이 실행된다 (들여쓰기된 코드들)
print('무조건 실행되는 코드') #조건의 참, 거짓 상관없이 항상 실행
'''x는 5보다 크다
그래서, 조건문은 참이다
무조건 실행되는 코드'''

x = 3
if x > 5 :
    print('x는 5보다 크다')
    print('그래서, 조건문은 참이다')
print('무조건 실행되는 코드') 
'''x는 5보다 크다
그래서, 조건문은 참이다
무조건 실행되는 코드'''

x=120
if not 0<= x <=100:
    x=float('nan')
print('점수는 {}점 입니다.'.format(x)) # 점수는 nan점 입니다.

#if~else 문
# 양자 택일로 동작하는 조건문

x=120
if x>100:
    x=100
else:
    x=x
print('점수는 {}점 입니다.'.format(x)) # 점수는 100점 입니다.

#if~eiif~else문
#여러 조건을 연쇄적으로 참, 거짓을 판별하는 조건문
# else가 없어도 됨

x =-120
if x > 100:
    x=100
elif x< 0:
    x=0
else:
    x=x
print('점수는 {}점 입니다.'.format(x)) # 점수는 0점 입니다.

#중첩된 if문

math = 90
eng = 80
if math >=60:
    if eng >= 60:
        print('합격입니다.')
    else :
        print('영어점수 미달입니다.')
else:
    if eng >= 60:
        print('수학 점수 미달입니다.')
    else :
        print('두 과목 모두 미달입니다.')
# 조건 표현식
#if~else문을 한 줄로 줄이는 방법 (파이썬 style)
# 항상되는 것이 아닌, 변수에 표현식을 대입하는 경우에만 가능

x=120
x=100 if x > 100 else x
print (f'x ={x}') 

# for 반복문 (range)
# range는 슬라이싱과 유사하게 시작점 끝점+1, 스텝을 입력할 수 ㅇ

#i 변수에 0~9까지 총 10번 반복
for i in range(10) :
    print(i) # 1,2,3,4,5,6,7,8,9
    # print(i, end=' ') # 1,2,3,4,5,6,7,8,9 (가로로 출력)
for i in range(2, 8) : # i에 2이상 8미만까지 / 총 8-2번 반복 (슬라이싱 비슷)
    print(i) # 2,3,4,5,6,7
for i in range(2, 10, 3) : # i에 2이상 10미만까지 3씩 증가하면서 반복 (슬라이싱 비슷)
    print(i) # 2,5,8

# for문 반복자 (리스트, 튜플, 문자열, 집합, 딕셔너리 가능)
x = [10,20,30,40]
for i in x : #range 대신 반복자 (여러 자료를 갖고있는 변수로써, 하나씩 불러와서 반복)
    print(i) # 10, 20, 30, 40

x ={'a':100, 'b':200, 'c':300}
for key in x : #딕셔너리는 반복하면 key를 하나씩 순회한다
    print(key) # a,b,c
    #print(key, x[key]) # 이렇게하면 value를 가져올 수 ㅇ #a 100, b 200, c 300

# 중첩된 for문
# if문이 중첩되듯, for문도 중첩 가능

for i in range(3) : #i -> 0,1,2
    for j in range(2) : #j->0,1
       print(i, j) #3*2 = 6번 반복
'''0 0
0 1
1 0
1 1
2 0
2 1'''


# zip을 이용한 for문
a=[1,2,3]
b=[4,5,6]

# 2중 for문 (모든 조합을 전부 다 반복)
for i in a :
    for j in b : 
       print((i, j)) 
'''(1, 4)
(1, 5)
(1, 6)
(2, 4)
(2, 5)
(2, 6)
(3, 4)
(3, 5)
(3, 6)
'''
# zip을 이용한 for문 (같은 인덱스끼리만 반복)/ 파이썬에만 있음
for i,j in zip(a,b) :
    print((i, j)) #(1, 4) (2, 5) (3, 6)

x=[10,20,30,40,50] # 인덱스와 value를 동시에 얻을 수 있음
for i, val in enumerate (x) :
    print(i, val)

# 대부분의 언어는 아래와 같은 방법으로 접근
'''for i in range (len(x)) :
    val = x[i]
    print(i, val)
'''

# While문을 이용한 조건
#반복횟수가 정해지지 않음 (for문은 반복횟수가 정해져 ㅇ)
#무한루프되면 Ctrl c로 정지
# for -> while 변환 가능 / 반대는 안 될수도 ㅇ
x=1
while x < 100 :
    print(x)
    x+=10

#무한루프
# while True:
#   print(무한루프)
    
# for -> while 변환 (for문을 쓸 수 ㅇ면 for문이 컨트롤이 쉬우므로 for문 사용)
for i in range(2,10):
    print(i)

i=2
while i < 10: #i는 2부터 시작해서 10미만까지 반복
    print(i)
    i+=1

# 반복문의 제어문
#break, continue

#break..즉시 반복문을 종료 
for i in range(10):
    if i==3:
        break
    print(i) #0,1,2

#continue..현재 실행문만 건너뛰고 다음 반복으로 넘어감
for i in range(10):
    if i==3:
        continue
    print(i) #0,1,2,3,4,5,6,7,8,9 


for i in range(3):
    for j in range(3):
        if i==1:
            break # 가장 가까운 반복문에 동작..j-for문이 종료 ...
        print(i,j) #0 0, 1 0, 2 0

for i in range(3):
    for j in range(3):
        if i==1:
            continue # 가장 가까운 반복문에 동작..j-for문이 종료 ...
        print(i,j) #0 0, 0 2,1 0,1 2,2 0,2 2

#심화 
#가장 가까운 for문
for i in range(3):
    is_done = False

    for j in range(3):
        if j==1:
            is_done = True
            break # 가장 가까운 반복문에 동작..j-for문이 종료 ...
        print(i,j) 
    if is_done is True:
        break
print() #0 0


# 지능형 리스트
# List comprehension
# for문과 유사한 문법으로 리스트를 손쉽게 생성

# 0 2 4 6...18 를 요소로 가지는 리스트를 만들어보자
x=[]
for i in range(10):
    x.append(2*i)
print(x)

x=[2*i for i in range(10)]
print(x)

#Truely Falsy 값
x=[1,2,3,4,5]
while x: # x가 텅 비면 Falsy값이 되어 종료
    val =x.pop() # x 리스트에서 값을 하나씩 삭제
    print(val) #5,4,3,2,1

x = None # None은 Falsy값
if not x: # Falsy값이면 강제로 0으로 변경
    x = 0
print(x) #0

