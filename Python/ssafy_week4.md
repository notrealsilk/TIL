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
