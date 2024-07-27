# Fundamentals of Python

### 표현식​(Expression)
값으로 평가될 수 있는 코드 조각

### 값​(Value)
표현식이 평가된 결과

### 평가(evaluate)
표현식을 실행하여 값을 얻는 과정
>평가를 해야 값이 나옴

### 타입(Type)
- 피연산자 = 값
- 연산자

```
 Numeric Types
 Sequence Types (list, tuple, range)
 Text Sequence Type (str (문자열)
 Non-sequence Types (set, dict)
 None, Boolean, Functions..
```

### 변수 할당
표현식으로 변수에 값을 저장

### 객체 (Object)
타입을 갖는 메모리 주소 내 값 (값이 들어있는 상자)

### 연산자 우선순위 예시
```
# -16
-2 ** 4
>> **를 먼저 실행하고 -를 실행

# -16
-(2 ** 4)

# 16
(-2) ** 4
```
---------------------------------------------------------
# Numeric Types 

## int 정수형
### 진수 표현

'''
print(0b10) # 2 / 2진수

print(0o30) # 24 / 8진수

print(0x10) # 16 / 16진수
'''

## float 실수형
### 부동소수점 에러(Floating point rounding error)
정확히 동일한 값이 출력되지 않음
```
# 해결 전
a = 3.2 - 3.1 # 0.1
b = 1.2 - 1.1 # 0.1
print(a)  # 0.10000000000000009
print(b)  # 0.09999999999999987
print(a == b)  # False



# 해결 후
from decimal import Decimal # 모듈

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a)  # 0.1
print(b)  # 0.1
print(a == b)  # True
```

-------------------------
# Sequence Types
여러 개의 값을 순서대로 나열, not 정렬

순서(Sequence) / 인덱싱(Indexing) / 슬라이싱(Slicing) / 길이(Length) / 반복(Iteration)..반복문

### str(불변)
### list
### tuple(불변) : 파이썬 내부 동작 / `my_tutel_2 = (1,)`
### range(불변) : 정수 시퀀스 생성

----------------------
# Non-sequence Types
순서와 중복이 없음

### dict (키 불변)
### set
`my_set = set()` : 빈 세트 만들기

`my_dic = {}` : 빈 딕셔너리 만들기

```
#### 세트의 집합 연산
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

## 중복이 없어서 연산 가능

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```
### None
### Boolean

## Collection
- 여러 개의 항목 또는 요소를 담는 자료 구조
- str, list, tuple (시퀀스 자료형)/  set, dict (non 시퀀스 자료형)

-------------------------------------
# Type Conversion
한 데이터 타입을 다른 데이터 타입으로 변환

### 암시적 형변환 `Implicit Type conversion`
: 정수가 실수로 변환

### 명시적 형변환 `Explicit Type conversion`
: 프로그래머가 직접 형변환

---------------------
# 단축평가
논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작

(이미 앞에서 결과가 나왔으면 뒤의 연산은 하지않고 결과 결정)

#### 단축평가 예시 문제

```python
vowels = 'aeiou'

print(('a' and 'b') in vowels)  # False / 'b' in vowels (평가가 b에서 일어남)
print(('b' and 'a') in vowels)  # True / 'a'in vowels (평가가 a에서 일어남)

print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0 (0이 F므로 뒤는 안보고 앞에만 봄).. 단축평가/ 뒤를 봐도 결과가 달라지지 않으므로
print(0 and 0)  # 0 (0이 F므로 뒤는 안보고 앞에만 봄).. 단축평가

print(5 or 3)  # 5 / 단축평가
print(3 or 0)  # 3 / 단측평가
print(0 or 3)  # 3 
print(0 or 0)  # 0 / 단축평가 x
```
- and
    - 첫 번째 피연산자가 False인 경우, 전체 표현식은 False로 결정. 두 번째 피연산자는 평가되지 않고 그 값이 무시
    - 첫 번째 피연산자가 True인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정. 두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환

- or
    - 첫 번째 피연산자가 True인 경우, 전체 표현식은 True로 결정. 두 번째 피연산자는 평가되지 않고 그 값이 무시
    - 첫 번째 피연산자가 False인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정. 두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환

----------------------------------------------
# 함수 `Functions`

#### 매개변수(parameter)

: 함수 정의 시, 함수가 받을 값을 나타내는 변수

#### 인자(argument)

: 함수 호출 시, 실제로 전달되는 값

#### **`map(function, iterable)`**
첫번째 위치인자로 함수를 받고, 두번 째 위치인자를 반복이 가능한 객체(요소)를 받음..컬렉션(튜플, 리스트)
```python
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']
```
#### zip(*iterable)
임의의 iterable(반복가능(컬렉션)한 인자)을 모아 튜플을 원소로 하는 zip object를 반환
    ```python
    girls = ['jane', 'ashley']
    boys = ['peter', 'jay']
    pair = zip(girls, boys)

    print(pair)  # <zip object at 0x000001C76DE58700>
    print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')]
    ```
#### List Comprehension
# List Comprehension
리스트 생성 방법

'''
#### List Comprehension 구조
[expression for 변수 in iterable] # 반복을 돌면서 리스트를 만듦
list(expression for 변수 in iterable)

[expression for 변수 in iterable if 조건식]
list(expression for 변수 in iterable if 조건식)

```
```
#### List Comprehension 사용 전/후 비교

# 빈 리스트에 number의 요소를 하나씩 넣는 코드

- 사용 전
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = []

    for num in numbers:
        squared_numbers.append(num**2)

    print(squared_numbers)  # [1, 4, 9, 16, 25]
    ```

- 사용 후
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [num**2 for num in numbers]

    print(squared_numbers)  # [1, 4, 9, 16, 25]
    ```
    ```

#### LEGB Rule
- 파이썬에서 사용되는 이름(식별자)들은 특정한 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아 나가며, LEGB Rule이라고 부름

    1. Local scope : 지역 범위(현재 작업 중인 범위)
    2. Enclosed scope : 지역 범위 한 단계 위 범위
    3. Global scope : 최상단에 위치한 범위
    4. Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용할 수 있는 모든 것)

# 패킹, 언패킹
- `*`
    - 패킹 연산자로 사용될 때, 여러 개의 인자를 하나의 튜플로 묶음
    - 언패킹 연산자로 사용될 때, 시퀀스나 반복 가능한 객체를 각각의 요소로 언패킹하여 함수의 인자로 전달
- `**`
    - 언패킹 연산자로 사용될 때, 딕셔너리의 키-값 쌍을 언패킹하여 함수의 키워드 인자로 전달

--------------------------------------------------------------------------------------
# 제어문 `Control Statement`

- 조건문
    - if, elif, else
- 반복문
    - for, while
- 반복문 제어
    - break(반복 즉시 중지), continue(다음 반복으로 건너뜀), pass(넘어감)

# 조건문
`if` statement

# 반복문
`for` statement
```
#### 반복 가능한 객체 `iterable`
- 반복문에서 순회할 수 있는 객체
(시퀀스 객체 뿐만 아니라 dict, set, str, range 등도 포함)
```
`while` statement
: 종료 조건 필요








