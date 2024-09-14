##6장

#if문

"""
if 조건1:
    실행 명령문1
elif 조건2:
    실행 명령문2
elif 조건3:
    실행 명령문3
else:
    실행 명령문4 # 위 모든 조건들에 해당하지 않을 때 실행
    """

weather = input("오늘 날씨는 어때요? ")

if weather == "비" or weather == "비": # == / 조건문 끝에 : 붙이기
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요") # 2번
else:
    print("준비물 필요 없어요")

    #input() ; 사용자로부터 어떤 값을 입력받는 용도


temp = int(input("기온은 어때요? "))

if 30 <= temp: # 30 도 이상이면
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
# 위 비교 문장은 이렇게도 작성 가능합니다.
# elif 0 <= temp < 10:
    print("외투를 챙기세요")
else: # 그 외의 모든 경우 (0도 미만이면)
    print("너무 추워요. 나가지 마세요")

## for문 : 반복대상에서 값을 하나씩 꺼내서 반복 작업 수행

"""
for 변수 in 반복대상:
    실행 명령문1
    실행 명령문2
"""

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no)) # {0} 위치에는 waiting_no 의 값이 들어가요
"""
대기번호 : 0
대기번호 : 1
대기번호 : 2
대기번호 : 3
대기번호 : 4
"""

#range() : 연속된 정수 데이터를 생성

for waiting_no in range(1, 6): # 1부터 6직전까지 (1~5)
    print("대기번호 : {0}".format(waiting_no))
"""
대기번호 : 1
대기번호 : 2
대기번호 : 3
대기번호 : 4
대기번호 : 5
"""

## while문 : 조건이 만족하는 동안 끝없이 반복

"""
while 조건:
    실행 명령문1
    실행 명령문2
    실행 명령문3
"""

customer = "토르" # 손님
index = 5 # 부르는 횟수, 총 5회

while index >= 1: # 부르는 횟수가 1 이상인 경우에만 반복 실행
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))    
    index -= 1 # 부르는 횟수 감소
    if index == 0: # 5번 모두 불렀다면
        print("커피는 폐기처분되었습니다.")

"""
#무한루프 (컨트롤 c 누르면 강제 종료)
customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
    index += 1 #index에 1씩 더하기
"""


customer = "토르"
person = "Unknown"

while person != customer: # != :  같음을 확인하는 연산자
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")

    """
    !=로 인해 'person 값이 customer 값과 같을 때까지 반복(while)한다' 는 의미가 되고
person의 input 값에 다른 값을 넣으면 다시 반복, 토르를 넣으면 조건에 맞으니 while 문을 탈출하게 되는 거네요!
    """

##continue와 break

absent = [2, 5] # 결석한 학생 출석번호
no_book = [7] # 책을 가져오지 않은 학생 출석번호

for student in range(1, 11): # 출석번호 1~10번
    if student in absent: # 결석했으면 책을 읽지 않고 다음 학생으로 넘어가기
        continue
    elif student in no_book: # 책을 가져오지 않았으면 바로 수업 종료 (반복문 탈출)
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))


## 한 줄 for

students = [1, 2, 3, 4, 5]
print(students) # [1, 2, 3, 4, 5]

# 한 줄 for 를 이용하여 각 항목에 100 을 더함

students = [i + 100 for i in students] 
"""students 리스트에 있는 값을 불러오면서 거기에 100을 더한 값을 리스트로 바꿔라"""
print(students) # [101, 102, 103, 104, 105]




#학생 이름을 길이로 변환 / len() : 문자열이나 값의 길이

students = ["Iron man", "Thor", "I am groot"]
print(students) # ["Iron man", "Thor", "I am groot"]

# 한 줄 for 를 이용하여 각 이름의 길이 정보로 변환
students = [len(i) for i in students] 
"""
길이에 사용된 i라는 변수는 students 안의 값을 하나씩 가져오면서 추출한 길이의 값을 넣겠다.
"""
print(students) # [8, 4, 10]




#학생이름을 대문자로 변환 / upper() : 소문자를 대문자로

students = ["Iron man", "Thor", "I am groot"]
print(students) # ["Iron man", "Thor", "I am groot"]

# 한 줄 for 를 이용하여 각 이름을 대문자로 변경
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']


## 6강 퀴즈

"""
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다. random()
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[O] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[O] 3번째 손님 (소요시간 : 5분) 
...
[  ] 50번째 손님 (소요시간 : 16분) 

총 탑승 승객 : 2 분

"""

from random import * #random 모듈 불러오기

cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): # 총 50분의 승객
    time = randrange(5, 51) # 5분 ~ 50분 사이의 소요 시간
    
#randrange() : 난수 함수

    if 5 <= time <= 15: # 5분 ~ 15분 사이의 손님의 경우 매칭 성공
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 성공 정보 출력
        cnt += 1 # 총 탑승 승객 수 증가 처리
    else: # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 실패 정보 출력

print("총 탑승 승객 : {0}분".format(cnt))





