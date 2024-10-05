## Authentication System 1

- Cookie & Session

# Cookie & Session

## HTTP

HTML과 같은 리소스를 가져올 수 있게 해주는 규약

웹(`WWW`)에서 이뤄지는 모든 데이터 교환의 기초

### 특징

- **비연결 지향 (connectionless)**

: 서버는 요청에 대한 응답을 보낸 후 → 연결 끊음

- **무상태 (stateless)**

: 연결을 끊는 순간 클라이언트-서버 간 통신이 끝나며 상태 정보가 유지되지 x

### ※ 상태가 없다

: 장바구니에 담은 상태 유지 x

: 로그인 상태 유지 x


## 쿠키 (Cookie)

**서버가 사용자의 웹 브라우저에 전송하는 데이터 조각**

---

: 서버가 제공, 클라이언트에 저장되는 작은 데이터 파일

: 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

### 쿠키 동작 예시

1. 브라우저(=클라이언트)가 웹 서버에 웹 페이지 **요청**
2. 웹서버는 **[요청된 페이지+쿠키]** 응답을 브라우저에게 전송
3. 브라우저는 **[쿠키+쿠키속성(만료 시간, 도메인, 주소 등)]**을 저장소에 저장
4. 이후 브라우저가 같은 요청을 하면 **[해당 저장된 쿠키+요청]**을 전송
5. 웹 서버는 받은 쿠키 정보 확인, 사용자 식별, 세션 관리 
6. 웹 서버는 **[응답+ 새로운 쿠키 or 기존 쿠키 수정]** 해서 응답

---

- 쿠키를 이용한 장바구니 예시
1. 장바구니에 상품 담기
2. 개발자 도구에서 확인

3. 쿠키 데이터에서 확인 ㅇ
- Application > Cookies에서 확인 ㅇ

4. 메인 페이지 이동 → 장바구니 유지 확인


5. 빈 장바구니 상태를 개발자 도구에서 확인

  



### 쿠키의 작동 원리와 활용

### 1. 쿠키 저장 방식

: 브라우저(클라우드)는 쿠키를 **키-값의 데이터 형식**으로 저장

: 쿠키에는 추가 속성(만료시간, 도메인, 경로)이 포함 o

### 2. 쿠키 전송 과정

서버 → HTTP 응답 헤더의 Set-Cookies 필드를 통해 클라이언트에게 쿠키 전송

브라우저 → 받은 쿠키 저장, 동일한 서버에 재요청 시, **HTTP Header의 Cookie 필드에 저장된 쿠키**와 함께 전송

### 3. 쿠키의 주요 용도

: 두 요청이 동일한 브라우저에 들어왔는지 판단 → 사용자의 로그인 상태 유지

: **상태(stateless)가 없는 HTTP 프로토콜에서 상태 정보를 기억**시켜줌

---

<aside>
💡

즉, **쿠키는 매 요청마다 로그인된 사용자라는 인증 정보가 담긴 쿠키를 매 요청마다 보내는 것**

</aside>

### 쿠키 사용 목적

### 세션 관리 (Session management)

: 로그인, 장바구니 등 정보 관리

### 개인화 (Personalization)

: 사용자 선호 설정 저장

### 트래킹 (Tracking)

: 사용자 행동을 분석, 기록

## 세션 (Session)

서버 측에서 생성, 클라이언트-서버 간의 상태 유지

상태 정보를 저장하는 데이터 저장 방식

>> 쿠키에 세션 데이터를 저장, 매 요청시마다 세션 데이터를 함께 보냄


---

- **서버** → 세션 데이터 생성, 저장 / 세션 ID(데이터 접근 가능하게 하는 키)를 생성 / 클라이언트에 ID 전달
- **클라이언트** → 쿠키에 ID 저장 / 클라이언트가 같은 서버에 재요청할 때마다 (저장된 쿠키+요청+세션 ID) 전송

<aside>
💡

ex) 로그인 상태 유지를 위해 로그인 돼 있다는 사실을 입증하는 데이터를 **매 요청마다 계속해서 보냄** (이정도 예시 정도 알면 됨)

</aside>

### 목적

클라이언트-서버 간의 상태 정보 유지, 사용자 식별 ㅇ

---

- Django Authentication System (인증 시스템) / Custom User model

# Django Authentication System

사용자 인증과 관련된 기능을 모아 놓은 시스템

## Authentication (인증)

사용자가 자신이 누구인지 확인하는 것 (신원 확인)

---

cf) **권한** : 인증된 사용자가 무엇을 사용할 수 있는지 (인증 후에 작동)

### 사전 준비

### 두번째 app accounts 생성, 등록

: auth와 관련한 경로나 키워드들을 **django 내부적으로 accounts라는 이름으로 사용**하고 있기 때문에 되도록 **‘accounts’로 지정하는 것을 권장**


# Custom User model

- 기본  user model의 한계
  

  : django에 내장된 auth앱에 작성된 User 클래스를 사용했음
  
  ---
  
  **but, 제공 필드 제한적 + User Model 변경이 어려움**
  

- 내장된 auth 앱

## Custom User model 대체하기

- 프로젝트의 특정 요구사항에 맞춰 사용자 모델을 확장 ㅇ

ex) 이메일을 username으로 사용, 다른 추가 필드를 포함 시킬 수 ㅇ

### 과정

### 1. AbstractUser 클래스를 상속받는 커스텀 User 클래스 작성

: 기본 usr 클래스도 AbstractUser를 상속받음 

→ 커스텀  user 클래스도 기존 user 클래스와 완전히 같은 모습을 가지게 ㅇ


- `앱(accounts)/models.py`

```python
## 앱의 accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# 커스텀 User 모델로 대체하기 위한 class 작성
class User(AbstractUser):
  pass
```

### 2. 기본 user 모델을 직접 작성한 User 모델로 사용할 수 있게 AUTH_USER_MODEL 값 작성

- `프로젝트/setting.py`

```python
## 프로젝트/setting.py

# user 모델을 직접 작성한 것으로 변경하겠다.
AUTH_USER_MODEL = 'accounts.User'
```

### 3. admin site에 대체한 User 모델 등록

: 기존 User 모델이 아니여서 등록안하면 admin 페이지에 출력되지 않기 때문

- `앱(accounts)/admin.py`


```python
## accounts 앱/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# 두번째 인자로 UserAdmin 가져오기
admin.site.register(User, UserAdmin)
```

>> 두번째 인자로 UserAdmin 클래스 가져오기

### 사용하는 user 테이블 변화


>> accounts_user에 사용자 정보가 앞으로 저장됨

---

### `AUTH_USER_MODEL`

Django 프로젝트의 User를 나타내는 데 사용하는 모델을 지정하는 속성

<aside>
💡

### ! 주의 !

**프로젝트 중간에 AUTH_USER_MODEL를 변경할 수 x**

: 앱, 설정 등은 서로 얽혀있기 때문에 모델만 변경하면 안되고 변경할 요소가 많음…

**>> 즉, 이미 프로젝트 진행되고 있으면 DB 초기화 후 진행**

</aside>

---

### 프로젝트를 시작하며 반드시 user 모델을 대체해야 o

- 장고는 새 프로젝트를 시작하는 경우, USER 모델이 충분해도 커스컴 USER 모델을 설정하는 것을 강력히 권장

>> 커스텀 USER 모델 : **기본 USER 모델과 동일하게 작동**+필요한 경우 **나중에 맞춤 설정**할 수 있기 때문

<aside>
💡

단, User 모델 대체 작업은 프로젝트의 모든 **migarations or 첫 migrate를 실행하기 전에** 작업을 마쳐야 ㅇ

</aside>

---

- Login / Logout

<aside>
💡

로그인 : GET 요청 / a태그 사용

로그아웃 : POST 요청 / form태그 사용

</aside>

# Login

로그인  = Session을 Create하는 과정

- CRUD의 Create

---

### `AuthenticationForm()`

로그인 인증에 사용할 **데이터를 입력받는 built-in form**

- 로그인 form (모델 form이 아님)

..로그인은 데이터베이스에 저장하지 X

cf)  회원가입= Model  Form사용..사용자가 입력한 데이터를 저장 ㅇ

## 1. 로그인 페이지 작성

- **GET** → 로그인 페이지
- **POST** → 인증 / 로그인 진행

>> create처럼 하나의 로직으로 합치기 가능


## 2. 로그인 로직 작성


form 클래스(request, request.POST(=데이터))

: 로그인은 form을 사용하므로 인자 순서 주의!

cf) ModelForm하고 다름! 

---

login view 함수와  django의 login 함수 이름이 겹치므로 `as` 를 사용해서 auth_login 으로 이름 바꿔주기

### `login(request, user)`

AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수

### `get_user()`

AuthenticationForm의 인스턴스 메서드

>> 유효성 검사를 통과했으면, 로그인한 사용자(=인증된 사용자) 객체 반환

## 3. 세션 데이터 확인

1. 로그인 후 발급받은 세션 확인

> django_session 테이블에서 확인


1. 브라우저에서 확인

> 개발자 도구 → Application → Cookie
 

>> session이 매 요청마다 같이 보내짐 

## 로그인 링크 작성

: 메인 페이지에 로그인 페이지로 갈 수 있는 링크 작성

# Logout

로그아웃 = Session을 Delete하는 과정

---

### `login(request)`

1. DB에서 현재 요청에 대한 Session Data를 삭제
2. 클라이언트의 쿠키에서도 Session Id를 삭제

## 로그아웃 로직 작성

- 로그아웃 진행 및 세션 데이터 삭제 확인

- Template with Authentication

# Template with Authentication

템플릿에서 로그인 여부를 확인 어렵

>> Django에선 로그인 여부를 템플릿에 출력할 수 있게 기능을 내장 ㅇ = `Template with Authentication data`

## Template with Authentication data

템플릿과 인증 데이터

: 템플릿에서 인증 관련 데이터를 출력하는 방법

## 현재 로그인 되어있는 유저 정보 출력

- user라는 context 데이터를 사용할 수 있는 이유

>> django가 미리 준비한 context 데이터가 존재하기 때문 (context processor)

(context processor)

>> user.username이라는 필드는 없지만 사용 가능

## context processors

- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 템플릿에서 사용 가능한 변수로 포함 ㅇ
- django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것
  

<aside>
💡

>> user.username이라는 필드는 없지만 사용 가능한 이유 = context processors

---

즉, 모든 곳에서 user를 사용가능 (따로 안 불러내도 됨)

</aside>

---

- 로그인, 로그아웃 코드

```python
##앱 accounts/views.py

from django.shortcuts import render, redirect
# 로그인할 떄 사용하는 form 가져오기
from django.contrib.auth.forms import AuthenticationForm
# 인증된 사용자의 세션 데이터 생성-> 로그인 동작하는 함수
from django.contrib.auth import login as auth_login
# 로그아웃 함수
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
  if request.method == 'POST':
      form = AuthenticationForm(request, request.POST)
      if form.is_valid():
          # 만약 인증된 사용자라면 로그인 진행(세션데이터 생성)
          # auth_login(request, 인증된 유저 객체)
          # form.get_user()..is_valid를 통과한 인증된 유저 객체를 택함
          
          auth_login(request, form.get_user())
          return redirect('articles:index')
  else:
      form = AuthenticationForm()
  context = {
      'form': form,
  }
  return render(request, 'accounts/login.html', context)

def logout(request):
  # 세션 데이터 삭제
  auth_logout(request)
  return redirect('articles:index')
  

```

- 참고

## 쿠키의 수명

1. 창을 끄면 로그아웃
2. 창을 꺼도 로그인 유지

>> 즉, 쿠키 종류에 따라 다름



### 쿠키와 개인정보 보호

- 많은 국가에서 쿠키 사용에 대한 사용자 동의를 요구하는 법규 시행 ㅇ
- 웹사이트는 쿠키 정책을 명시, 필요한 경우 사용자 동의 얻어야 ㅇ


## AbsturactUser class

관리자 권한과 함께 완전한 기능을 가지고 있는 User mode을 구현하는 추상 기본클래스


---

## User 모델 대체하기 Tip

user 모델을 대체하는 순서를 숙지하기 어려울 경우, 해당 공식문서를 보며 순서대로 진행하는 것을 권장
