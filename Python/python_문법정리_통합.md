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


# 메서드

`help` () .. 함수가 정의된 class를 볼 수 있음

**데이터타입 object.method()**

# 시퀀스 데이터 구조

## 문자열

is~().. T or F 반환하는 함수인 경우가 많음 

원본을 바꾸지 않음 
>> str은 불변이기 때문에 원본을 조작한 새로운 문자열 결과를 반환

```markdown
##### 메서드 이어서 사용하기 (Chaining)
- 모든 메서드는 이어서 사용 가능

```python
text = 'heLLo, woRld!'

new_text = text.swapcase().replace('l', 'z')

print(new_text) # HEzzO, WOrLD!
```
```

단, 이어사용할 때, 각 메소드가 데이터타입과 맞아야함



## 리스트

reverse()는 정렬이 아님!!

L.sort() 리스트정렬

## 딕셔너리 메소드

- 딕셔너리 생성 `a={}`

- get 메소드

```markdown
키 접근법 : [] 접근, get메소드 사용
get은 키가 없으면 반환값으로 None반환 (에러 안 일으킴)
```

- keys 메소드

```python
person = {'name': 'Alice', 'age': 25}
print(person.keys()) 
# dict_keys(['name', 'age']) 
# -> 리스트 형식이므로 시퀀스형식이구나 
# -> 반복 진행하면 키값을 가져올 수 있겠구나

for item in person.keys():
    print(item)
# name
# age
```

- items 메소드

```
person = {'name': 'Alice', 'age': 25}
print(person.items()) # dict_items([('name', 'Alice'), ('age', 25)])..튜플

for item in person.items():
    print(item)
# ('name', 'Alice')
# ('age', 25)

for key,value in person.items(): # 언패킹
    print(key)
    print(value)
    
# name
# Alice
# age
# 25
```

## 세트 메소드

- 세트 생성 `a=set()` / 세트는 순서없음
    

    - `pop()`
    
    : 해시 테이블에 나타나는 순서대로 반환
    
    : “임의” =  (해시테이블에 배치되는 것 자체가 정해져있지않음) / 무작위의 의미가 아님

## 객체 지향 프로그래밍

데이터 + 데이터를 조작하는 메서드(데이터의 행위)를 하나의 객체(클래스)로 묶어 관리

## 절차 지향 프로그래밍

코드의 순차적 흐름과 함수의 순서대로 작동

---

# 클래스

파이썬에서 타입을 표현하는 방법

객체를 생성하기 위한 설계도 (데이터+메서드)

: 클래스 이름은 파스칼 케이스(MyClass) 방식으로 작성

## 객체

클래스에서 정의된 것을 토대로 메모리에 할당된 것

속성(attribute)(=데이터)과 행동(method)(=메서드 = 함수)으로 구성된 모든 것

## 인스턴스

클래스로 만든 객체

클래스에 정의된 메서드를 .으로 호출 가능+ 클래스 안의 속성 호출가능

- 데이터가 메서드를 호출

인스턴스.메서드()

객체.행동()

## 클래스 구조

### 생성자 메서드 `__init__()`

### 클래스 변수

클래스가 호출하는 메서드

class.class 변수로 클래스 변수 참조

### 인스턴스 변수

독립적인 값을 가짐

### 인스턴스 메서드

# 메서드

## 메서드 종류

### 인스턴스 메서드

인스턴스 상태를 변경, 해당 인스턴스의 특정 동작을 수행

```python
class Person:
    def __init__(self, name) :
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 매서드의 매개변수 name
        self.name = name
        # self.ssafy = name 도 가능
        print('인스턴스 생성완료')
        
    def greeting(self) :
        print(f"안녕하세요 {self.name} 입니다.") # 인스턴스 변수를 호출해야함

person1 = Person("지민")
person1.greeting() # self 매개변수는 작성할 필요없음
# = Person.greeting(person1) ## 파이썬 내부에서는 위의 두 표현식을 이렇게 작동함

# 인스턴스 생성완료
# 안녕하세요 지민 입니다.
```

- str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것

>> 반드시, 첫번 째 메개변수로 인스턴스 자신(self)를 전달받음

### 생성자 메서드 `__init__()`

인스턴스가 객체 생성할 때, 자동으로 호출되는 메서드

```python
class Person:
    def __init__(self, name) :
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 매서드의 매개변수 name
        self.name = name
        # self.ssafy = name 도 가능
        print('인스턴스 생성완료')
        
    def greeting(self) :
        print(f"안녕하세요 {self.name} 입니다.") # 인스턴스 변수를 호출해야함

person1 = Person("지민")
person1.greeting() # self 매개변수는 작성할 필요없음
# = Person.greeting(person1) ## 파이썬 내부에서는 위의 두 표현식을 이렇게 작동함

# 인스턴스 생성완료
# 안녕하세요 지민 입니다.
```

### 클래스 메서드 `@classmethod`

인스턴스의 상태에 의존하지 않는 기능을 정의 / 클래스 변수 조작, 클래스 레벨의 동작 수행

---

`@classmethod` 데코레이터를 사용해 정의 (함수를 꾸미는 기능..함수의 기능을 추가)

호출 시, 첫번째 인자로 cls가 전달됨 >> 이름 바꾸면 안됨

```python
class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
        
    @ classmethod
    def number_of_popluation(cls):
        print(f'인구수는 {cls.count}입니다.') 
        # 아직 이때는 클래스 안에 정의된 함수가 아님
        

person1 = Person('iu')
person2 = Person('BTS')

# 이때 number_of_popluation()의 클래스가 Person으로 결정
Person.number_of_popluation() # 인구수는 2입니다.
```

### 정적(static) 메서드 `@staticmethod`

인스턴스와 상호작용이 필요하지않은 일반적인 기능을 수행

필수적으로 작성해야 할 매개변수 없음

클래스가 정적 메서드를 호출하기에 인스턴스 없어도 됨

>> 객체 상태나 클래스 상태 수정을 할 수 없고, 단지 행동만을 위한 메서드로 사용(like 일반함수)

```python
class StringUtils:
    # 생성자 메서드 안에 기능, 속성이 없어도 되지만, 생성자 메서드를 pass를 쓰더라도 써야함
    def __init__(self) :
        pass
    
    @staticmethod
    def reverse_string(string):
        return string[::-1]

    @staticmethod
    def capitalize_string(string):
        return string.capitalize()
    

text = 'hello, world'

result1 = StringUtils.reverse_string(text)
print(result1) # dlrow ,olleh

```

### 절차지향과 객체 지향은 대조되는 개념이 아니다

: 절차지향을 보완하는 형식이 객체 지향(상속, 코드 재사용성, 유지보수성)!!

# 상속

기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성

하위클래스 = 기존클래스 속성, 메서드 + 새로운 속성, 메서드

:  상위클래스의 인스턴스 메서드/클래스 메서드/스테틱 메서드 모두 상속가능

## 단일상속

부모 클래스 1개

`Class 자식 클래스(부모클래스) >> 상속`

## 다중상속

부모 클래스가 2개 이상

중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

>> **MRO(Method Resolution Order) 알고리즘**을 사용하여 클래스 목록을 생성

: 부모 클래스로부터 상속된 속성들의 검색을 **깊이 우선**으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음

```markdown
    ```python
    class D(B, C):
        pass
    ```
    # 속성이 D 에서 발견되지 않으면, B 에서 찾고, 거기에서도 발견되지 않으면, C 에서 찾고, 이런 식으로 진행됨
```

### **MRO(Method Resolution Order) 메서드 결정 순서**

**`super()`** 부모 클래스 객체를 반환하는 내장 함수

: 다중 상속 시 상위 클래스를 MRO를 기반으로 가져옴

```markdown
##### super의 2 가지 사용 사례
1. 단일 상속 구조
    클래스 이름이 변경되거나 부모 클래스가 교체되어도 super()를 사용하면 코드 수정이 더 적게 필요
2. 다중 상속 구조
    - MRO 순서대로 메서드 호출
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제를 방지
```

```markdown
#### super() 사용 예시 (다중 상속)

```python
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'

    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'

    def show_value(self):
        print(f'Value from ParentB: {self.value_b}’)

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # ParentA 클래스의 __init__ 메서드 호출
        self.value_c = 'Child’

    def show_value(self):
        super().show_value() # ParentA 클래스의 show_value 메서드 호출
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()
```
```

```python
# 자식 클래스에서 부모 클래스의 클래스 메서드 호출하기

# 부모클래스
class Animal:
    total_count = 0

    def __init__(self, name):
        self.name = name
        Animal.total_count += 1

    # 클래스 메서드
    @classmethod
    def get_total_count(cls): # 클래스 메서드를 호출하는 클래스(cls가 뭔지는 아직 모름)
        return f'전체 동물 수: {cls.total_count}'

# 자식 클래스
class Dog(Animal):
    dog_count = 0 # 클래스 변수

    def __init__(self, name, breed):
        super().__init__(name) # Animal 클래스의 생성자메서드를 상속 받음
        self.breed = breed
        Dog.dog_count += 1

    @classmethod
    def get_dog_info(cls):
        # cls.get_total_count()는 부모 클래스의 클래스 메서드를 호출하여 전체 동물 수를 출력
        return f'{cls.get_total_count()}, 강아지 수: {cls.dog_count}'

class Cat(Animal):
    cat_count = 0

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        Cat.cat_count += 1

    @classmethod
    def get_cat_info(cls):
        # cls.get_total_count()는 부모 클래스의 클래스 메서드를 호출하여 전체 동물 수를 출력
        return f'{cls.get_total_count()}, 고양이 수: {cls.cat_count}'

dog1 = Dog('멍멍이', '삽살개')
dog2 = Dog('바둑이', '진돗개')
print(Dog.get_dog_info())  # 출력: 전체 동물 수: 2, 강아지 수: 2

cat1 = Cat('노아', '페르시안')
cat2 = Cat('루비', '코숏')
print(Cat.get_cat_info())  # 출력: 전체 동물 수: 4, 고양이 수: 2

```

```markdown
#### `mro()` 사용 예시

  ```python
  class A:
      def __init__(self):
          print('A Constructor')

  class B(A):
      def __init__(self):
          super().__init__()
          print('B Constructor')

  class C(A):
      def __init__(self):
          super().__init__()
          print('C Constructor')
          
  class D(B, C):
      def __init__(self):
          super().__init__()
          print('D Constructor')

  print(D.mro())
  ```
```
### 에러 `Error`

프로그램 실행 중에 발생하는 예외 상황

- 문법 에러 `Syntax Error`

```markdown
#### 문법 에러 예시
- Invalid syntax (문법 오류)
    
    ```py
    while # SyntaxError: invalid syntax
    ```

- assign to literal (잘못된 할당)
    
    ```py
    5=3 # SyntaxError: cannot assign to literal
    ```

- EOL (End of Line)
    
    ```py
    print('hello   
    # SyntaxError: EOL while scanning string literal
    ```

- EOF (End of File)
    
    ```py
    print(
    #SyntaxError: unexpected EOF while parsing
    ```

```

### 예외 **`Exception`**

 프로그램 실행 중에 발생하는 예외 상황

### 예외처리
```markdown
- `try`
  - 예외가 발생할 수 있는 코드 작성
- `except`
  - 예외가 발생했을 때 실행할 코드 작성
- `else`
  - 예외가 발생하지 않았을 때 실행할 코드 작성
- `finally`
  - 예외 발생 여부와 상관없이 항상 실행할 코드 작성
```

`except` 를 상속클래스에 사용시, 하위 클래스부터 예외 사용을 작성해야함
