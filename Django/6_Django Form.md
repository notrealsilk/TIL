`<form>` 태그 역할:

1. `action`: 데이터를 서버로 전송할 URL
2. `method`: 데이터 전송 방식 (GET/POST)

※ 유효성 검사는 불가

# Django Form

사용자 입력 데이터를 **수집, 처리, 유효성 검사**를 수행하는 도구

---

>> 유효성 검사를 단순화 하고 자동화 할 수 있는 기능을 제공

>> HTML form생성, 데이터 유효성 검사, 처리를 쉽게 할 수 있도록 도움

### 유효성 검사

수집한 데이터가 정확, 유효한 지 확인하는 과정

>> 유효성 검사할 때는 많은 것을 고려해야 하기에 Django의 Form을 사용

## Form class

- 정의

>> 앱 폴더에 직접 생성해줘야 ㅇ


- `forms` 에는 `TextField`가 없음 > 그래서 `CharField()` 사용

### Form class를 적용한 new 로직


>> `{{ form }}` 이 라벨까지 다 만들어줌


### Form rendering options

label, input 쌍을 특정 HTML 태그로 감싸는 옵션


### `.as_p`
>> `p` 태그로 감싸주면 title과 content가 떨어짐


---

즉, form class로 사용자 입력부분을 대체할 수 있음


## Widgets

HTML `input` 요소의 표현 담당 / input의 표현을 바꾸는 것!

### Widget 적용

: content 크기가 커짐


# Django ModelForm

Model과 연결된 Form을 자동으로 생성해주는 기능 제공 / `Form + Model`

<aside>
💡

- Form

: 사용자 입력 데이터를 DB에 저장하지 않을 때 

예)) 검색, 로그인

- ModelForm
: 사용자 입력 데이터를 **DB에 저장**

예)) 게시글 작성, 회원가입 

</aside>

---

### ModleForm class 코드

- 코드

### 정의


: 기존 Article Form 클래스를 수정

### 적용
  
: `Modelform` 에 있는 class를 해석해서 form 태그를 자동 적용 

### ModelForm class가 대체하는 것


## Meta Class

ModelForm의 정보를 작성하는 곳

<aside>
💡

### Meta data

: 데이터의 데이터

예)) 사진을 찍음 

>> 사진의 메타 데이터 = 위치, 조도, 조리개값 등..

</aside>

즉, modelform의 추가 정보, 속성만 작성한 것

---

### `fields` , `exclude` 속성

exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음

### 주의사항

- 장고 **modelform에 대한 추가 정보나 속성을 작성**하는 클래스 구조를 Meta클래스로 작성한 것 뿐

>> 문법적인 관점으로 접근하면 X


## ModelForm 적용

### ModelForm 적용한 create

- is_ valid()

### `is_valid()`

여러 유효성 검사 실행 → 데이터가 유효한 지 여부를 Boolean으로 반환


- 별도로 명시하지 않았지만, Model 필드에는 빈 값을 허용하지 않음
- 빈 값은 is_valid()에 의해 false로 평가, Form 객체에는 그에 맞는 에러 메시지가 포함되어 다음 코드로 진행 ㅇ

---

: 데이터 저장 전에 `is_valid()` 를 통해 유효성 검사!

- 유효성 검사 통과하면 redirect로 다른 html로 보냄
- 유효성 검사를 실패한 폼이면 다시 new html을 보냄

>> 실패한 폼이면 `is_valid()` 가 실패한 이유를 폼에 담아서 보내줌.. 이걸 context에 담아서 new html과 함께 다시 보냄


---

- modelform을 사용하지 않는 경우


어떤 데이터를 받는 지 일일히 변수 지정 할 필요 없음

---

제목 `input` 에 공백을 입력 → 제출 시 에러 메세지 출력 확인 → 유효성 검사의 결과


### ModelForm 적용한 edit


### ModelForm 적용한 update


---

### `save()`

DB 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드

: 키워드 인자 **instance** 여부를 통해 saved의 생성, 수정을 결정

# HTTP 요청 다루기

## View 함수 구조 변화

HTTP request method 차이점을 활용해 동일한 목적을 가지는 2개의 view함수를 **하나로** 구조화

## new & create 함수 결합

<aside>
💡

### new & create view 함수

- 공통점

: 데이터 생성을 구현 / `C`RUD

- 차이점

: `new` 는 GET method 요청만을,

: `create` 는 POST 요청만을 처리

</aside>

### 새로운 create view 함수

1. new 와 create view 함수의 공통점, 차이점을 기반으로 하나로 결합

: 코드 작성시, else문 부터 작성해야 흐름대로 작성하는 것

- else부분은 new함수 그대로 쓰기
- get, post 말고 다른 메서드가 있기 때문에 if문은 요청이 post일 때와 아닐 때로 나뉜다.

---

1. 차이점이었던 request method에 따른 분기

1. POST 일 때는 과거 create 함수 구조였던 객체 생성 및 저장 로직 처리
        
2. POST가 아닐 때는 과거 new 함수에서 진행했던 form 인스턴스 생성
  

3. context에 담기는 form은
  
  : is_valid()를 통과하지 못한 에러메세지를 담은 form이거나
  
  : else문을 통한 form 인스턴스
      

### 기존 new 관련 코드 수정

- 사용하지 않게 된 new url 제거


: view 함수가 create로 하나로 합쳐져서 제거해도 ㅇ

- new 관련 키워드 → create로 변경


- render에서 new 템플릿→ create 템플릿으로 변경
          


---


## edit & update 함수 결합

---

### 기존 edit 관련 코드 수정

- 사용하지 않는 edit url 제거
          
- edit 관련 키워드 → update로 변경
## ModelForm 키워드 인자 구성

### 모델폼의 구성

- data는 첫번째에 위치한 키워드 인자여서 생략 ㅇ
- instance는 9번째에 위치한 키워드 인자여서 생략 x
