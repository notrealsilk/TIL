### 부트스트랩 사이트
https://getbootstrap.com/

---

# Bootstrap

CSS 프엔 프레임워크 (도구 모음)

: 특정한 규칙이 있는 클래스 이름으로 스타일, 레이아웃이 미리 작성 ㅇ

>> 공식 문서 꼭 같이 보면서 사용!!

---

- CDN 코드(content Delivery Network)

: 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화

(사용자와 가까운 cdn 서버에 콘텐츠를 저장해서 사용자에게 전달)

: cdn 2개 코드로 불러옴 (`bootstrap.min.css`, `bootstrap.bundle.min.js`)

```html
CSS 프레임워크 -> 남들이 만들어놓은 코드
- 가져오는 방법1. 설치를 하는 방법
  -> 실습 10개 할 때, 10번 다운로드 해야한다!!!
- 가져오는 방법2. 실시간으로 인터넷을 통해 가져오는 방법
  -> 서버로부터 데이터를 받아옴.

   - 서버가 외국에 있다!
      - 우리는 한국에 있어서, 서버와의 거리가 매우 길어진다.
      -> 느리다. 불안정하다.
   -> 서버를 복사해서 가까이 두자! ex) 한국서버
  -> 한국 사람들은 가까운 한국 서버로
  -> 미국 사람들은 가까운 미국 서버로 요청을 보내자
   - 이렇게 사용되는 기술이 CDN (Contents Delivery Network)
```

## Bootstrap  기본 사용

부트스트랩은 style을 class로 만들어 놓음!

---

### 예)) `<p class=”mt-5”>Hello, world!</p>`

**m** {property}**t**{sides}**-5**{size}

(marge(속성), top(방향), 사이즈)



- property : 속성
- sides : 4방향 (왼쪽 `l` 오른쪽 `e`)
- size : `rem` 단위

<aside>
💡 `rem` 이란?? 

>> 웹 사이즈의 기본 단위 (반응형 웹사이트를 위해 `rem` 단위를 사용)
: 픽셀로 하면 브라우저 환경에 따라 크기가 달라짐.. 통일성 위해 `rem` 사용

</aside>

## Reset CSS

HTML 요소, 테이블, 리스트 등의 요소에 일관성 있는 스타일을 적용시키는 기본 단계

: 브라우저마다 설정이 상이 `user agent stylesheets`하므로, 모두 똑같은 스타일 상태 만들고 스타일 개발을 시작하자는 취지 (( ..일종의 리셋 ))

### Normalize CSS

: Reset CSS의 대표적 방법 / 정규화!!

: 웹 표준 기준으로 브라우저 중 하나가 불일치, 차이가 있는 브라우저를 수정

: 불일치한 브라우저에 맞춰서 나머지를 그에 맞게 수정하기도 ㅇ

---

: 부트스트랩은 `bootstrap-reboot.css` 파일명으로 Normalize CSS를 자체적으로 제공

# Bootstrap 활용

>> 공식 문서 꼭 같이 보면서 사용!!

## Typography

- Display headings : 눈에 띄는 제목
  
  
- Inline text elements : inline 요소 스타일
  
  
- Lists : list 요소 스타일
  
  

## Colors

- Text colors
  
  
- Background colors
  
  

## Component

- Ui 관련 요소 (버튼, 네비게이션바, 카드, 폼, 드롭다운..)
- 일관된 디자인으로 사이트 구성요소 구축에 활용

(Button, Navbar, Modal)

<aside>
💡 **- Alerts : 경고 메세지 나타내는..

- badges

- Buttons

- Cards (많이 사용)

- navbar

- carousel
: carousel id 속성 값과 각 버튼의 data-bs-target 속성 값이 각각 올바르게 일치하는지 확인

- Modal
: 모달은  코드 깊은 곳에 넣지말고, 코드 아랫쪽에 모아두는게 좋음
: 모달과 모달의 버튼은 같이 있을 필요 없음**

</aside>

- Semantic Web

# Semantic Web

웹 데이터를 의미론적으로 구조화된 형태로 표현 (요소의 목적과 역할)

---

- 검색엔진 최적화(SEO)

웹 사이트 분석 쉽게해서 검색 순위에 영향 줌 + 개발자가 이해하기 쉬움

: 다양한 태그 써서 만든 웹사이트가 더 분석이 쉬움..

- 웹 접근성(Web Accessibility)

다양한 사용자가 사용할 수 있게 설계, 개발

고령자, 장애를 가진 사용자들이 사용할 수 있도록 설계 및 개발 (예)) 스크린 리더)

## OOCSS (object oriented css)

객체 지향적 방법으로 css 구성하는 방법론 (css방법론 중 하나..)

: CSS를 유지보수가 용이하게 작성하기 위한 가이드라인

- 기본원칙 : 구조와 스킨 분리 / 컨테이너와 콘텐츠를 분리

### 구조와 스킨 분리

재사용성 높이기

예)) 버튼과 색 구조를 따로 분리


### 컨테이너와 콘텐츠를 분리

객체를 둘러싼 컨테이너에 스타일 적용, 위치에 의존하는 스타일을 사용하지 않음

콘텐츠를 다른 컨테이너로 이동, 재배치할 때 스타일 깨지는 것을 방지

(독립적인 스타일 적용!!!)


## Bootstrap 사용 이유

: 많이 사용 / 빠른 개발, 유지보수 / 손쉬운 반응형 웹 디자인 구현 / 커스터마이징 / 크로스 브라우징(모든 브라우저에서 작동 ㅇ)
