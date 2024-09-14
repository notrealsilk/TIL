# CSS Layout (inner display type)

각 요소의 위치와 크기를 조정 >> 웹 페이지 디자인!

(display, position, flexbox를 사용 / 오른쪽으로 갈수록 최신 기술)

- css box model (dispaly)

# CSS Box Model

웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델, 요소의 크기와 배치를 결정

>> 내용(content), 안쪽 여백(padding), 테두리(border), 외부간격(margin)


<aside>
💡 **CSS Box Model의 속성 = 박스 구성요소

- content box**
실제 콘텐츠가 표시되는 영역 크기
width 및 height 속성을 사용해서 크기 조정

**- padding box**
콘텐츠 주위에 위치하는 공백 영역

**- border box**
콘텐츠와 패딩을 감싸는 테두리 영역 (border 속성으로 조정)

**- margin box**
박스와 다른 요소 사이의 공백 (가장 바깥쪽 영역)

</aside>

## shorthand 속성

속성을 한번에 지정


상우하좌 조심!!!

## box-sizing 속성

### standard box model (표준 상자 모델) / content-box

: width, height 속성값 = content box 크기

: 기본 설정

### alternative box model (대체 상자 모델) / border-box

: width, height 속성값 = content box + padding box + border box 크기

<aside>
💡 보통 border-box기준으로 상자 모델을 사용 (그래야 작업하기 수월)

so,  `*` 을 사용해서 작업하기 전에, 기본값인  content-box를  border-box로 바꿔줌

</aside>

- css position

# CSS Position

요소를 normal flow(outer display box..inline,block)에서 제거해서 다른 위치로 배치

(즉, 다른 요소 위에 요소 얹기, 특정 위치에 요소를 옮기기 등..)

- 이동방향이 5방향임
  

<목적> 페이지의 특정 항목의 위치를 조정

## Position 유형

### static

: 요소를 normal flow에 따라 배치

: top, right, bottom, left 속성이 적용되지 않음

: 기본값

### relative

: 요소를 normal flow에 따라 배치

: 자신의 원래 위치(static)기준으로 이동

: top, right, bottom, left 속성으로 위치 조정

: 다른 요소의 레이아웃에 영향을 주지 않음 (요소가 차지하는 공간은 static때와 같음.. 상대위치)

### absolute

: 절대위치 (요소를 normal flow에서 제거)

: 가장 `가까운 relative 부모 요소`를 기준으로 이동 (만족하는 부모 요소가 없으면 `body 태그`를 기준으로 함)

: top, right, bottom, left 속성으로 위치 조정

: 문서에서 요소가 차지하는 공간이 없어짐 (그래서 다른 요소가 치고 올라 올 수 ㅇ)

### fixed

: 절대위치 (요소를 normal flow에서 제거)

: 현재 화면영역(viewport)을 기준으로 이동

: 스크롤해도 항상 같은 위치에 유지

: top, right, bottom, left 속성으로 위치 조정

: 문서에서 요소가 차지하는 공간이 없어짐

예)) 위로 가기 버튼

### sticky

: `ralative`+ `fixed`의 특성 결합

: 스크롤 위치가 임계점에 도달 전 - `ralative`처럼 동작

: 임계점에 도달 -  `fixed`처럼 화면에 고정

: 만약 다음 sticky 요소가 나오면, `다음 sticky 요소`가 이전 sticky 요소의 자리를 대체

(이전 sticky 요소가 고정되어 있던 위치와 다음 stick요소가 고정되어야 할 위치가 겹치게 되기 때문)

## z-index

: 요소의 쌓임 순서(stack order)를 정의하는 속성

: 정수 값을 사용해  z축 순서를 지정

: 값이 클수록 요소가 위에 쌓임 / static이 아닌 요소에만 적용 (그러나 부모요소보다 값이 클 수 없으므로 자식 요소의 값을 아무리 높여도 부모요소 값이 작다면 요소가 위로 가지않음)

: z-index 숫자가 높을수록 위로 감

- css flexbox

# CSS Flexbox

**lnner display type / 일종의 큰 그림 그리기**

: 박스 내부 요소들이 어떻게 배치될 지를 결정

- 요소를 행과 열 형태로 배치하는 1차원 레이아웃 방식 **(공간 배열과 정렬)**

: flex박스는 부모 박스(flex container)를 만들면서 시작

## 구성요소

1. flex container(부모 박스) 만들고, 그 안에 flex ltem(자식박스) 만듦
2. **메인 축 기준**으로 교차 축이 결정 (축을 돌릴 수 ㅇ)

### main axis

flex item들이 배치되는 기본 축

: main start → main end방향으로 배치 (기본값)

### cross axis

메인 축에 수직인 축

: cross start → cross end방향으로 배치 (기본값)

### Flex Container (부모 요소)


: 부모 요소를 선언하는 순간, 그 안에 있는 요소는 자연스레 자식요소가 됨 (따로 자식 요소 선언할 필요 없음)

: 부모요소가 배치하는 주체 (배치하는 주체!!가 flexbox)

### Flex ltem (자식 요소)


: **lnline 속성을 가짐**

: 자식을 움직이고 싶으면 부모를 움직여라!!!

## Flexbox 속성

### flex container 관련 속성

: flex item(자식요소)는 기본적으로 행(주 축=기본값인 가로방향)

- 배치

`flex direction`

: 열의 주 축이 변경 / `-reverse` 지정하면 item 배치의 시작(s), 끝(e)이 바뀜 

```html
    /* flex 선언.. 선언하면 자식요소가 flex item이 됨 */
    /* 높이 설정을 따로 하지 않으면 부모요소 높이만큼 자식요소가 차지 */

    display: flex; 
    
    /*기본 설정..가로(행), 왼 -> 오*/
    flex-direction: row; 
    /* flex 축 바꾸기..세로(열)*/
    flex-direction: column; 
    /* flex 방향이 오-> 왼 */
    flex-direction: row-reverse;
     /* flex 방향이 아래 -> 위 */
    flex-direction: column-reverse;
```

`flex-wrap`

: item 목록이 한 행에 들어가지 않을 경우, 다른 행에 배치할 지 여부 결정

```html
    /* 기본값 */
    /* flex-wrap: nowrap; */
    
    /* item의 행 바꿈을 원할 때 설정 */
    /* flex-wrap: wrap; */
```

- 공간분배 (정렬)

`justify-content`

: 주 축을 따라 flex item과 주위에 공간을 분배

```html
    /* !!메인축!! 주 축을 기준으로 배치 */
    
    /* 기본값 */
    /* justify-content: flex-start; */
    /* 가운데 정렬 */
    /* justify-content: center; */
    /* 오른쪽 정렬 */
    /* justify-content: flex-end; */
```

`align-content`

: 교차 축을 따라 flex item과 주위에 공간을 분배 (한 줄 짜리 행에는 효과 없음)

```html
    /* !!교차축!! 배치..wram에 따라 달라짐 */
    /* 교차축을 기준으로 위 정렬, 가운데 정렬, 아래 정렬이 됨 */
    
    /* align-content: flex-start;
    align-content: center;
    align-content: flex-end; */
```

- 정렬

`align-item`

: 교차 축을 따라 flex item을 정렬

```html
    /* 한 줄 정렬 위, 중간, 아래*/
    
    /* align-items: flex-start; */
    /* align-items: center; */
    /* align-items: flex-end; */
```

---

### flex item 관련 속성

`align-self`

: 교차 축을 따라 개별 flex item을 정렬

`flex-grow` <-> `flex-shrink`

: 남는 행 여백을 비율에 따라 각 flex item에 분배 (아이템이 컨테이너 내에서 확장하는 비율을 지정)


`flex-basis`

: flex item의 초기 크기 값을 지정 (width보다 flex-basis가 우선!)

: `width` 보다 우선!!!

### 목적에 따른 속성


- 배치 (크게 배치, 배치 방향 설정)
- 공간분배 (행, 열로 분배)
- 정렬 (디테일한 정렬).. 요소 하나씩 정렬 등..

### 속성 명 Tip

justify (주축) : `justify-content`

align (교차축) : `align-content` `align-item` `align-self`

## flex-wrap 응용

## 반응형 레이아웃

다양한 디바이스와 화면 크기에 자동으로 적응하여 콘텐츠를 최적으로 표시하는 웹 레이아웃 방식

: `flex-wrap` `flex-grow` `flex-basis` 활용

### justify-items 및 justify-self 속성이 없는 이유

필요없어서.. >> `margin auto`를 통해 정렬 및 배치가 가능



## Margin collapsing (마진 상쇄)


복잡한 레이아웃을 요소 간 간격을 일관 되게 유지하기 위함

요소 간의 간격을 더 예측 가능하고 관리하기 쉽게 만듦 >> 일관성, 단순화
