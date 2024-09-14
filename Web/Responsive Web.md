# Bootstrap Grid System

웹 페이지의 **레이아웃**을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템

<aside>
💡 12개의 컬럼(열)인 이유

1. 12는 약수가 많음 (1,2,3,4,6,12)
2. 적당히 큰 수..

</aside>

### <목적>

반응형 디자인을 지원.. 웹 페이지를 다양한 기기에서 적절하게 표시할 수 있도록 도움

---

- 반응형 웹 디자인(Responsive Web Design)

: 어떤 브라우저든 일관된 레이아웃 및 사용자 경험을 제공

## Grid System 구조

1. **Container** : column을 담고 있는 공간 (Grid System의 시작)
2. **Column** : 실제 컨텐츠를 포함하는 부분..12개
3. **Gutter** : 컬럼과 컬럼 사이의 여백 영역
4. 1개의 row안에 12개의 column 영역을 구성



## Grid System 실습

### 기본


- 코드

```html
<h2 class="text-center">Basic</h2>
<div class="container">
<!-- 하나의 행 안에 12개의 col을 몇 개씩 나눌 것인지.. -->
<div class="row">
  <div class="box col">col</div>
  <div class="box col">col</div>
  <div class="box col">col</div>
</div>
<div class="row">
  <div class="box col-4">col-4</div>
  <div class="box col-4">col-4</div>
  <div class="box col-4">col-4</div>
</div>
<div class="row">
  <div class="box col-2">col-2</div>
  <div class="box col-8">col-8</div>
  <div class="box col-2">col-2</div>
</div>
</div>
```


### 중첩(Nesting)

<div class="row"> 안에 <div class="row"> 또 선언


- 코드

```html
<!-- 중첩(Nesting) -->
<hr>

<h2 class="text-center">Nesting</h2>
<div class="container">
<div class="row">
  <div class="box col-4">col-4</div>
  <div class="box col-8">
    <!-- 새로운 행 시작 -->
    <!-- 열이 12개가 넘어가면 다음 칸으로 넘어감-->
     <!-- ctrl + alt 하면 커서 여러 개 -->
    <div class="row">
      <div class="box col-6">col-6</div>
      <div class="box col-6">col-6</div>
      <div class="box col-6">col-6</div>
      <div class="box col-6">col-6</div>
    </div>
  </div>
</div>
</div>

<hr>
```


### 상쇄(Offset)

- col 칸을 생략해서 비워두기


- 코드

```html
<hr>

<h2 class="text-center">Offset</h2>
<div class="container">
<div class="row">
  <!-- 4칸을 쓰고 4칸을 상쇄시키고 4칸을 생략해라 -->
  <div class="box col-4">col-4</div>
  <div class="box col-4 offset-4">col-4 offset-4</div>
</div>
<div class="">
  <div class="box col-3 offset-3">col-3 offset-3</div>
  <div class="box col-3 offset-3">col-3 offset-3</div>
</div>
<div class="">
  <!-- 6칸을 상쇄시키고 3칸을 생략해라 -->
  <div class="box col-6 offset-3">col-6 offset-3</div>
</div>
</div>

<hr>
```


### Gutters

- Grid System에서 column 사이에 여백 생성
- **x축은 padding**, **y축은 margin**으로 여백 생성

: x축은 (좌우)는 margin으로 밀어내지 않음 (margin쓰면 row을 넘어가서 안됨..)

- Gutters는 행(row)에 적용!!


- 코드

```html
<!-- Gutters -->
<!-- gutter는 row에 적용 -->
<hr>

<h2 class="text-center">Gutters(gx-0)</h2>
<div class="container">
<!--gx-0..(x축에 0여백) x축은 padding에 여백-->
<div class="row gx-0">
  <div class="col-6">
    <div class="box">col</div>
  </div>
  <div class="col-6">
    <div class="box">col</div>
  </div>
</div>
</div>

<br>

<h2 class="text-center">Gutters(gy-5)</h2>
<div class="container">
<!--gy-5..y축은 margin에 여백-->
<div class="row gy-5">
  <div class="col-6">
    <div class="box">col</div>
  </div>
  <div class="col-6">
    <div class="box">col</div>
  </div>
  <div class="col-6">
    <div class="box">col</div>
  </div>
  <div class="col-6">
    <div class="box">col</div>
  </div>
</div>
</div>

<br>

<h2 class="text-center">Gutters(g-5)</h2>
<div class="container">
<!--g-5..x,y축에 5 여백-->
<div class="row g-5">
  <div class="col-6">
    <div class="box">col</div>
  </div>
  <div class="col-6">
    <div class="box">col</div>
  </div>
  <div class="col-6">
    <div class="box">col</div>
  </div>
  <div class="col-6">
    <div class="box">col</div>
  </div>
</div>
</div>
```

- Grid system for responsive web

# Grid system for responsive web

Bootstrap Grid System에서는 12개의 column과 6개의 breakpoints를 사용하여 반응형 웹 디자인을 구현

## Grid system Breakpoints

웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점

: 화면 너비에 따라 6개의 분기점 제공 (xs, sm, mg, lg, xl, xxl)..Grid system 클래스랑 같이 씀

---

최대 너비 값 “이상”


## Breakpoints 실습

- 코드

```html
  <h2 class="text-center">Breakpoints</h2>
  <div class="container">
    <div class="row">
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
        col
      </div>
      <div class="box col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
        col
      </div>
    </div>
```


---

\
- 코드

```html
    <h2 class="text-center">Breakpoints + offset</h2>
    <div class="row g-4">
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <div class="box col-12 col-sm-4 col-md-6">
        col
      </div>
      <!-- sm이 되는 순간 offset-sm-4 "이상"일 때 적용 -->
       <!-- md사이즈에서는 offset없애고 싶으면 제거 설정해줘야 함..offset-md-0 -->
      <div class="box col-12 col-sm-4 offset-sm-4 col-md-6 offset-md-0">
        col
      </div>
    </div>
  </div>
```


## CSS Layout 정리

Grid system / Flexbox / position 등..

각각 고유한 특장점이 있음(상호보완적)

>> 즉, 최적의 기술, 효과적 활용이 중요

- UX UI

## UX (user experience)

사용자의 전체적인 경험과 만족도를 개선하고 최적화하기위한 디자인, 개발 분야

- 유저의 마음과 생각을 이해, 정리 >> 제품으로 만드는 과정
- 유저 리서치, 데이터 설계 및 정제, 유저 시나리오, 프로토타입 설계

## UI (uset interface)

서비스와 사용자 간의 상호작용을 가능하게 하는 디자인 요소를 개발, 구현

- 사용자가 더 쉽고 편하게 사용할 수 있도록 고려 (사용자가 고민하지않고 사용 가능하도록..)
- 디자인 시스템, 중간 산출물, 프로토타입 필요
- 참고

## The Grid System

구성 요소를 잘 배치해서 시각적으로 좋은 결과물을 만들기 위함

- 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에 기인
- 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

## Grid Cards

row-col 클래스를 사용해 행당 표시할 카드 수를 손쉽게 제어

---

# 반응형 웹 사이트 구현

디바이스 크기에 따라 웹 페이지 요소가 달라져야 한다.

- 웹 페이지를 설계 할 때는 <<**상단 메뉴바 / 메인컨텐츠 / 꼬리말**>> 이 기본 틀

---

배치와 관련된 반응형 (grid system)..12칸 사용해서

부모자리에 클래스를 row, 자식 자리에 클래스를 col해주면 됨

## 웹 페이지 설계

### 메뉴바

```html
<nav></nav>
```

### 메인 컨텐츠

<div></div> .. 지양해야함 

<aside>
💡 **<div></div>를 지양해야하는 이유??**
1. 유지보수가 어려움
2. 검색엔진에 잘 걸리지 않음 (사이트 노출 이슈) SEO

SO, 시멘틱 태그를 써야함!!!

</aside>

```html
<main>
<section>
</section>
<article>
</article>
</main>
```

### 꼬리말

```html
<footer></footer>
```

### 자주 쓰는 태그

<table> <dl> <dt> <dd> <ul> <ol>..

---

### 시멘틱 태그를 얼마나 잘 썼는가??

이를 어떻게 판단할까??

**SEO checker**를 사용하면 됨!! https://www.seobility.net/en/seocheck/

### 부트스트랩

일반 css와의 차이점

1. 기본 마진이 사라짐
2. 텍스트 컬러가 안 먹힘

>> 그 이유.. 여러 환경에 놓인 개발자들이 사용하므로 reset 개념으로 이렇게 설정됨

---

### 구글 폰트 적용하기

css와 폰트 링크(html) 복붙해서 가져오기

---

### `@media` : 미디어 쿼리

: css에서 반응형을 구현할 수 있는 기능

@media 미디어타입 and(조건) {css 규칙}

`@` : at-rule

all 에는 디바이스가 들어감 (어느 디바이스에 적용할래? all, screen, print 등..)

- 조건

`min-width` : 최소 범위를 지정

`max-width` : 최대 범위를 지정
