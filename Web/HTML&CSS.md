### Web

: 사용자들이 정보를 검색하고 상호 작용하는 기술

### Web site

: 웹 페이지가 모인 공간

## Web page

: 웹사이트를 구성하는 하나의 요소

- html : 사이트 구조 (structure)
- css : 웹 사이트를 꾸밈 (styling)
- javascript : 웹 사이트의 작동 (behavior)

### 태그
`h태그` 헤더

`p태그` 내용 작성

`a태그` 하이퍼링크 연결할 수 있는 태그

`img` 이미지 주소(`src`)만 필요 / `alt` 이미지 대체 텍스트 / 닫는 태그 없음

`div` 웹 사이트의 레이아웃을 설정 / block 박스 (오른쪽 공간을 다 먹음 냠냠)

`span` 텍스트 내용이 들어간 부분만큼만 영역을 차지 / inline 

`em` 태그안의 태그 가능 / 기울림체

`strong` 볼드체

`ol` (순서가 있는)부모태그 

`li` 자식 태그(자식은 일촌 / 자손은 모두)

`ul` (순서가 없는) 부모태그

`input` 입력받는 태그 (텍스트, 비밀번호 등 속성 ㅇ)


---
# HTML (HyperText Markup Language)

: 웹 페이지의 의미와 구조를 정의하는 언어

- HyperText : 웹 페이지를 다른 페이지로 연결하는 링크 / 비선형성
- Markup Language : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

## HTML 구조

태그의 역할위주로 공부하기

vs 코드에서 `!`+ `tab`을 하면 기본 뼈대가 나옴


## HTML 속성

<aside>
💡 개발자 도구 키는 세가지 방법

마우스 오른쪽 > 속성

- `ctrl` `shift` `i`
- `F12`
</aside>



## HTML 의미

`<h1>Heading</h1>`

: 현재 문서의 최상위 제목이라는 의미 부여

`h1태그` 여러개를 써도 사이트에 뜨긴 함..스타일가이드에는 위배


---
# CSS (Cascading Style Sheet)

웹 페이지의 디자인과 레이아웃을 구성하는 언어

선언 순서에 따라 적용되는게 다름

## CSS 구문


: 요소(tag)선택자

문장 끝이 `;` 세미콜론으로 끝 (선언의 종료를 뜻함)

## CSS 적용 방법

**재활용의 관점에서 스타일을 선택**

1. **인라인(Inline) 스타일**
HTML 요소 안에 Style 속성 값으로 작성
: 잘 사용 안함
    
    
2. **내부(Internal) 스타일 시트**
head 태그 안에 style 태그에 작성
하나의 파일에서 중복으로 적용

    
3. **외부(External) 스타일 시트**
별도 css 파일 생성 후 HTML link 태그를 사용해 불러오기
: head 안에 넣기


## CSS 선택자 (css Selectors)

HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

클래스 안의 요소를 선택!

### CSS Selector 종류

### CSS Selectors 특징

- 전체 선택자`*`

: HTML의 모든요소를 선택

- 요소 선택자

: 지정된 모든 태그를 선택

:  요소 선택자 >> 전체 선택자

- 클래스 선택자 `.`

: 주어진 클래스 속성을 가진 모든 요소를 선택

(페이지 여러 곳에 중복 적용 ㅇ)

- 아이디 선택자 `#`

: 주어진 아이디 속성을 가진 요소 선택

: 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함

### CSS Combinators 특징

- 자손 결합자 `" " (space)`

: 첫 번째 요소의 자손 요소들 선택 

- 자식 결합자 `>`

: 첫 번째 요소의 직계 자식만 선택 (직계 자식 = 해당요소만!!)

선택자들 사이의 우선 순위 ㅇ

## 웹 스타일링

### 명시도(Specificity)

선언하는 순서대로 cascade

결과적으로 요소에 적용할  CSS 선언을 결정하기 위한 알고리즘

- CSS Selectors에 가중치를 계산하여 어떤 스타일 적용할 지 결정 (명시도 높은 Selectors기 적용)


- `! important` > line 스타일 > 선택자 (`#` > `.` > 요소(태그 선택자) > `*` 선택자) > 코드 선언 순서

---

- class 선택자를 주로 사용함

: 클래스는 여러 선택자에 사용 가능 (모든 태그마다 들어가 있음) <여러 요소에 재활용 가능>

: id 선택자는 한 번 사용 (여러번 사용해도 되는데 id 선택자의 의미상.. 그렇게 씀) <하나의 요소에 사용>

- 예제
    
    ```html
    <!--   <p>1</p>
      <p class="orange">2</p>
      헤드에서 나중에 선언된 초록색이 우선
      <p class="green orange">3</p>
      <p class="orange green">4</p>
      아이디 선택자 우선
      <p id="red" class="orange">5</p>
      !important가 적용
      <h2 id="red" class="orange">6</h2>
      인라인 스타일 우선 적용
      <p id="red" class="orange" style="color: brown;">7</p>
      !important
      <h2 id="red" class="orange" style="color: brown;">8</h2> -->
    ```
    

### 계단식(Cascade)

한 요소에 동일한 가중치를 가진 선택자를 적용될 때 CSS에서 마지막에 나오는 선언이 사용됨

### `!important`

최우선으로 적용하는 키워드

: cascade 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용을 권장하지 않음

## CSS 상속

상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임


## CSS Box Model

웹 페이지의 모든 html 요소를 감싸는 사각형 상자 모델

박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

<aside>
💡 **박스 타입 종류**

### Block box

오른쪽의 남은 여백을 다 차지

`h` `p` `div태그` 

### Inline box

본인이 가진 컨텐츠 넓이만 차지

예) `<a>` `img` `strong`

**Normal flow** : 일반적으로 웹 페이지 요소가 배치되는 방식


</aside>

## 박스 표시(display) 타입

## Outer display type

박스 바깥쪽

```html
/* 블록 요소로 변경 */
.element {
  display: block;
}

/* 인라인 요소로 변경 */
.element {
  display: inline;
}

/* 인라인 블록 요소로 변경 */
.element {
  display: inline-block;
}

/* 요소 숨기기 */
.element {
  display: none;
}

```


## Inner display type

박스 내부 요소를 정렬하는 방식

- Flex


### inline-block

inline과 block 요소 사이의 중간 지점을 제공하는 display 값

width 및 height 속성 사용가능

새로운 행으로 넘어가지 않음 / p,d,m로 인해 다른 요소가 상자에서 밀려남

>> 요소가 줄 바꿈 되는 것을 원하지 않으면서 너비와 높이는 적용하고 싶을 때 사용

### none

요소를 화면에 표시하지 않고 공간을 부여하지 않음
