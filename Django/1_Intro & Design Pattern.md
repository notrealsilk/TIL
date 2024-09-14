# Web Application

인터넷을 통해 사용자에게 제공되는 sw 프로그램을 구축하는 과정

> 웹 브라우저를 통해 접근, 사용 O 

## 클라이언트와 서버

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/edd2c896-fb7e-49a2-8efb-99b725db9e13/%EC%BA%A1%EC%B2%98.png)

### Client

서비스를 요청하는 주체 (웹 사용자의 인터넷이 연결된 장치)

### Server

클라이언트의 요청에 응답하는 주체 (웹페이지, 앱을 저장하는 컴퓨터)

---

### 웹 페이지를 보게 되는 과정

1. 클라이언트(웹 브라우저)가 [`google.com`](http://google.com) 입력
2. 서버에게 `메인 홈페이지.html` 파일달라고 요청
3. 서버가 파일 찾아서 응답
4. 클라이언트는 전달받은 html를 사람이 볼 수 있게 해석→ 구글 페이지 접속 ㅇ

## Frontend & Backend

### Frontend

: UI를 구성하고, 사용자가 애플리케이션과 상호작용하게 함 / 클라이언트가 보는 부분

: HTML,CSS,JavaScript, 프엔 프레임워크..

### Backend

: 서버 측에서 동작, 클라이언트 요청에 대한 처리와 데이터베이스와의 상호작용 담당

: 서버언어 + 백엔트 프레임워크, 데베, API, 보안..

---

    
    # Web Framework
    
    웹 애플리케이션을 빠르개 개발할 수 있도록 도와주는 도구
    
    (개발에 필요한 기본구조, 규칙, 라이브러리 제공)
    
    ## Django Framework
    
    python 기반의 웹 프레임워크
    
    ![스크린샷 2024-09-12 오후 8.31.52.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/d4a334ed-21d8-4e42-a3d7-9e4cbdfc360a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2024-09-12_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_8.31.52.png)
    
    즉, Django 사용해서 서버를 구현 → 대규모 트래픽 서비스에서도 안정적인 서비스 제공
    
    ## 가상 환경
    
    Python 애플리케이션과 패키지들을 격리하여 관리할 수 있는 **독립적인** 실행 환경
    
    ![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/09ad9aa3-869e-4f13-9b87-df210efd5806/%EC%BA%A1%EC%B2%98.png)
    
    >> global 환경 안에 다른 환경들이 ㅇ / 다른 환경들은 서로 독립적! (연결된 프로그램이 다름) 
    
    ---
    
    ### 가상환경 생성방법
    
    1. 가상환경 venv 생성 
    
    `python -m venv venv` << 관례적으로 venv 이름 사용
    
    2. 가상 환경 활성화 (on-off 개념)
    - 가상환경 on
    
    `source venv/Scripts/activate`  .. source 뒤에 있는 경로의 파일에서 가상환경을 킬꺼야
    
    : (맥, 리눅스는 `source venv/bin/activate`)
    
    : `(venv)`가 뜨면 가상 환경 on 된 것
    
    : 환경이 설치된 패키지 목록 확인 명령어 >> `pip list`
    
    - 가상환경 off
    
    >> 1. 터미널을 그냥 끈다 2. `deactivate`를 입력한다. (보통 귀찮아서 그냥 끄는 경우가.. 많음)
    
    3. 설치된 패키지 목록 확인
    
    `pip freeze > requirements.txt`
    
    : 현재 파이썬 환경에 설치된 모든 패키지와 버전을 텍스트 파일로 저장
    
    : `requirements.txt`..생성될 파일 이름 (관례)
    
    <aside>
    💡
    
    - 이렇게 하는 이유
    
    .. venv의 파일 크기가 커서 설치된 패키지 목록을 다른 개발자에게 전달.. 다른 개발자는 이를 토대로 가상환경 셋팅함. 즉, 가상환경자체를 공유하지 않음
    
    `pip intall -r requirements.txt`로 가상환경이 활성화된 상태에서, 텍스트 파일에 작성된 목록 기반으로 설치
    </aside>
    
    ### 의존성 패키지
    
    한 소프트웨어 패키지가 다른 패키지의 기능, 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동 >> 패키자 설치 안됐더나, 호환버전이 아니면 작동이 제대로  x
    
    .. 하나의 패키지를 깔면 여러 패키지가 같이 깔리는데 그 이유가 의존성 패키지 때문..
    
    >> 개발 환경에서는 각각의 프로젝트가 사용하는 패키지와 그 저번을 정확히 관리하는 것이 중요
    
    ---
    
    가상환경 & 의존성 패키지 관리 중요!
    
    ## Django 프로젝트
    
    ### 1. Django 프로젝트 생성
    
    `django-admin startproject firstpjt .` >> firstpjt 이름의 프로젝트 생성
    
    ### 2. 서버 실행
    
    `python [manage.py](http://managr.py) runserver` >> manage.py와 동일한 경로에서 진행
    
    ### 3. 서버 확인
    
     http://127.0.0.1:8000/ 에 접속해서 확인


---
# Django Design Pattern

## Design Pattern

### 디자인 패턴

소프트웨서 설계에서 발생하는 문제를 해결하기 위한 해결책

>> 애플리케이션 구조는 이렇게 구성하자~~ 와 같은 관행

### MVC 디자인 패턴

(Model, View, Controller)

애플리케이션을 구조화하는 패턴

데이터, UI, 비지니스 로직을 분리

>> 시각적 요소와 로직을 서로 영향 없이, 독립적이고 유지보수가 쉬운 어플을 만들기 위해..

### MTV 디자인 패턴

(Model, Template, View)

디장고에서 어플을 구조화하는 패턴

---

- Model

: 데이터와 관련된 로직 관리

: 응용프로그램의 데이터 구조를 정의, 데베 기록 관리

- Template (mvc의 `v`)

: 레이아웃과 화면 처리

: ui구조와 레이아웃 정의

- View (mvc의 `c`)

: Template과 Model 사이에서 관련된 로직을 처리해서 응답 반환

: 클라이언트의 요청에 대해 처리를 분기함

## Project & App

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/6d333cdd-903d-45ac-9908-56bf220eb1d0/%EC%BA%A1%EC%B2%98.png)

### Project

애플리케이션의 집합

### App

: 독립적으로 작동하는 기능 단위 모듈 /  기능 단위로 나누기!

: 각자 특정 기능을 담당하며 다른 앱들과 함께 하나의 PJ을 구성

## App 사용 순서

### 1. 앱 생성

`$ python [manage.py](http://manage.py) startapp articles` 

… `python [manage.py](http://manage.py)`에 startapp acticles 이름의 앱을 실행할거야~

: 복수형 이름 지향

: 프로젝트 폴더 안에 앱이 생성되는 것이 아님 (독립적 존재)

### 2. 앱 등록

: 반드시 앱 생성 후 등록!! (등록 후 생성 불가능)

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/29fab6ed-dd5b-4b47-b59d-b59592820afc/%EC%BA%A1%EC%B2%98.png)

>> 프로젝트 파일→ [`settings.py`](http://settings.py) → INSTALLED_APPS

..INSTALLED_APPS 안에 사용자가 정의한 건 위에, 내장 명령을 아래에 해야 명령 순서대로 작동+ 오류 났을 때 잡기 좋음

### 프로젝트 구조

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/c98d7790-87ef-4074-a00f-b3c6cc7b8966/%EC%BA%A1%EC%B2%98.png)

`settings.py`

: 프로젝트의 모든 설정 관리

`urls.py`

: 요청 들어오는 url에 따라 이에 해당하는 view를 연결

### 앱 구조

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/e2da0c5e-132e-4b7d-933d-e1be36cbdf2c/%EC%BA%A1%EC%B2%98.png)

`admin.py`

: 관리자용 페이지 설정

[`models.py`](http://models.py) (M)

: DB관련된 Modle을 정의

[`views.py`](http://views.py) (V)

: HTTP 요청을 처리, 해당 요청에 대한 응답 반환 

: 실질적인 로직이 작성되는 곳

(url, model, template와 연계)

---

<aside>
💡 Template가 없는 이유

- 장고는 기본적으로 벡엔드 프레임워크이기 때문에 안 보여짐
- 보통 장고로 벡엔드, 다른 프레임워크로 프엔쪽을 작성하기때문
- 하지만 장고는 풀스텍 프레임워크를 지원 ㅇ
</aside>

---
# Django에서의 요청과 응답

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/473baec8-8f57-4c8f-ba2d-0be763adbb82/%EC%BA%A1%EC%B2%98.png)

### 데이터가 흐르는 순서

: 흐르는 순서대로 코드를 작성해야 디버깅에 용이

`URLs → View → Template`

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/b395a6cd-4675-4b5b-8130-b07260cb3a1d/%EC%BA%A1%EC%B2%98.png)

## 요청과 응답

### 1. URLs

: 요청이 오면, request 객체를 views 모듈의 index view 함수에게 전달하며 호출

![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/77845ce5-f435-45f4-910a-45acc69106bd/%EC%BA%A1%EC%B2%98.png)

### 2. View

: view 함수가 정의되는 곳

: 특정 경로에 있는 template와 request 객체를 결합해 응답 객체 반환

: 모든 view함수는 첫번쨰 인자로 요청 객체를 필수적으로 받음

### 3. Template

: 폴더명은 반드시 templates여야 하며, 개발자가 직접 생성해야 ㅇ

1. articles 앱 폴더 안에 template 폴더 생성
2. templates 폴더 안에 articles 폴더 생성
3. articles 폴더 안에 템플릿 파일 생성

---

    
    ## 가상환경 생성 루틴
    
    ![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/4f9bf3f4-d838-4fb9-9140-cc567e707b37/%EC%BA%A1%EC%B2%98.png)
    
    ### 가상환경 사용 이유
    
    - 의존성 관리 (독립적 사용가능)
    - 팀 프젝 협업 (모든 팀원이 동일한 환경 → 버전간 충돌 방지)
    
    ## Django 관련
    
    ### LTS (Long-Term Support)
    
    : 프레임워크, 라이브러리 등 sw에서 장기간 지원되는 안정적인 버전을 의미
    
    : sw 업그레이드에는 많은 비용, 시간이 필요하기에 안정적, 장기간 지원되는 버전이 필요
    
    : 장고의 4버전의 경우, `4.2`
    
    ## render 함수
    
    주어진 템플릿 객체를 통해 응답 객체를 반환하는 함수
    
    ![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/f73d570c-13e1-439c-8947-d56527b55abb/%EC%BA%A1%EC%B2%98.png)
    
    ## Trailing Comma
    
    ![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/0d3215c4-d47e-4028-a8c9-083e9e14b1de/%EC%BA%A1%EC%B2%98.png)
    
    **후행 쉼표**, 자료구조(리스트, 딕셔너리, 튜플 등)에서 마지막 요소 뒤에 쉼표를 추가하는 것 ..일반적으로 선택 사항
    
    : 새로운 요소 추가, 순서 변경에 편리
    
    : 값의 목록, 인자, import 항목들이 시간이 지남에 따라 확장될 것으로 예상되는 경우에 사용
    
    : 코드 가독성, 유지 보수 향상
    
    ## 프레임워크 규칙 및 설계 철학
    
    ![캡처.PNG](https://prod-files-secure.s3.us-west-2.amazonaws.com/05a316eb-e82a-4d55-999b-fceb215af99f/964ba4c7-5330-4909-b921-53baa4ae4bea/%EC%BA%A1%EC%B2%98.png)
