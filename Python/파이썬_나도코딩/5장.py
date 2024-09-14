#5장

##리스트 : 순서를 가진 객체의 집합 []

#subway = [10,20,30] 
#subway1=10,subway2=20, subway3=30 : 각각의 변수를 리스트 하나로 표현

#index() : 문자열 순서 세어줌
subway=['유재석', '조세호','박명수'] #0번째, 1번째, 2번째
print(subway.index('조세호')) #1번째 #index() : 문자열 순서 세어줌

#append () : 리스트에 변수 추가
subway.append('하하') 
print(subway) #['유재석', '조세호','박명수','하하']

#insert(n, '') : 리스트 n번째에 변수 추가
subway.insert(1, '정형돈') 
print(subway) #['유재석','정형돈','조세호','박명수','하하']

#remove() : 리스트에 변수 삭제
fruit=['apple', 'banana', 'peach', 'melon']
fruit.remove('banana') #fruit[1]='strawberry' : 1번째 변수를 'n'으로 바꾸겠다.

#pop() : 리스트에서 뒤에 있는 변수 1개를 꺼냄
print(subway.pop()) 
#['유재석','정형돈','조세호','박명수']

#count() : 변수 갯수를 세줌
subway=['유재석', '조세호','박명수','유재석']
print(subway.count('유재석')) #2

#sort() : 정렬하는 함수
num_list = [5,2,4,3,1]
num_list.sort() #sort() : 정렬하는 함수
print(num_list) #[1,2,3,4,5]

#reverse() : 정렬 순서 뒤집기
num_list.reverse() #reverse() : 순서 뒤집기
print(num_list) #[5,4,3,2,1]

#clear() : 정렬 지우기
num_list.clear() #clear() : 모두 지우기
print(num_list) #[]

#리스트 변수에 정수형, 실수형, 문자열, boolean형 넣기
mix_list=['조세호',20, True]
print(mix_list) #['조세호',20, True]

#리스트+리스트 / extend()
num_list=[5,2,4,3,1]
num_list.extend(mix_list) #extend()
print(num_list) #[5,2,4,3,1,'조세호',20,True]



##사전 : 중괄호 사용{}
#(키에 대한 중복이 허용 안됨)

#{key1 : value1, key2 : value2} / key는 열쇠, value는 사물함 / key는 정수형, 문자형 사용가능

cabinet = {3: "유재석", 100: "김태호"} #3,100이 key, "유재석", "김태호"가 value

#사전에서 value 꺼내는 법 1: []로 꺼내기

print(cabinet[3]) #유재석 -> key 3 에 해당하는 value
print(cabinet[100]) #김태호 -> key 100 에 해당하는 value

#사전에서 value 꺼내는 법 2: get()로 꺼내기
print(cabinet.get(3)) #유재석

#get() 사용법 : # key 에 해당하는 값이 없는 경우 기본 값을 사용
print(cabinet.get(5,'사용가능'))

#사전 자료 안에 원하는 값이 있는지 없는지 확인하는 법 : in
print(3 in cabinet) # True
print(5 in cabinet)  # False

# key 는 정수형이 아닌 문자열도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

#업데이트 및 추가
print(cabinet) #{"A-3": "유재석", "B-100": "김태호"}

cabinet["A-3"] = "김종국" # key 에 해당하는 값이 있는 경우 업데이트 #[]에 key
cabinet["C-20"] = "조세호" # key 에 해당하는 값이 없는 경우 신규 추가
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 삭제 / del 사용
del cabinet["A-3"] # key "A-3" 에 해당하는 데이터 삭제
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력  / keys()
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력 / values()
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력 / items()
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 전체 삭제 / clear()
cabinet.clear()
print(cabinet) #{}


##튜플 () : 데이터 변경, 삭제 불가

menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

#튜플 : 한 줄에 여러 변수 값 선언
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 김종국 20 코딩


## 세트=집합 : 중복 허용 안함, 순서 보장 안함 / {} or set()

my_set = {1, 2, 3, 3, 3} # 중복을 허용하지 않으므로 3은 1번만 들어감
print(my_set) # {1, 2, 3}

#set()
java = {"유재석", "김태호", "양세형"} # 자바 개발자 집합
python = set(["유재석", "박명수"]) # 파이썬 개발자 집합

# 교집합 (java 와 python 을 모두 할 수 있는 개발자) / &, intersection()

print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 또는 python 을 할 수 있는 개발자) /  |, union()

print(java | python) # {'박명수', '유재석', '김태호', '양세형'}
print(java.union(python)) # {'박명수', '유재석', '김태호', '양세형'}

# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자) /  - , difference()

print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# java 개발자 삭제 (기존 개발자 : 유재석, 김태호, 양세형) / remove()

java.remove("김태호")
print(java) # {'유재석', '양세형'}


## 자료구조의 변경

#type() : 데이터 형태 확인

menu = {"커피", "우유", "주스"} #세트=집합
print(menu, type(menu)) # menu 의 type 정보 : set

#세트->리스트
menu = list(menu) # 리스트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : list  
#["커피", "우유", "주스"] <class 'list'>

#리스트->튜플
menu = tuple(menu) # 튜플 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : tuple
#("커피", "우유", "주스") <class 'tuple'>

#튜플->세트
menu = set(menu) # 세트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : set
#{"커피", "우유", "주스"} <class 'set'>

#random 모듈

#shuffle()..리스트 안의 데이터를 섞어줌
#sample()..리스트 내의 원하는 갯수 뽑아줌


from random import *
lst = [1,2,3,4,5]
print(lst) # 원본 리스트
shuffle(lst) # 리스트를 뒤섞기
print(lst) # 섞은 후 리스트
print(sample(lst, 1)) # 리스트 내에서 1개를 무작위로 뽑기



## 5장 퀴즈


"""
Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복은 불가
조건3 : random 모듈의 shuffle 과 sample 을 활용

(출력 예제)
 -- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
 -- 축하합니다 --
 """





from random import *

users = list(range(1, 21)) # range 를 list 로 바로 감싸면 한 줄 더 줄일 수 있어요!
shuffle(users)

chicken_winner = sample(users, 1) # 치킨 당첨자 1명 추첨
remain_users = set(users) - set(chicken_winner) # 전체 집합에서 치킨 당첨자 집합을 제외
coffee_winners = sample(remain_users, 3) # 남은 19명 중에서 3명 추첨

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(chicken_winner))
print("커피 당첨자 : {0}".format(coffee_winners))
print("-- 축하합니다 --")